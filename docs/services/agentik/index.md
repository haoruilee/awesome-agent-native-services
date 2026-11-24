---
title: "Agentik | Agent-Native Services"
service_name: "Agentik"
description: "The tool gateway for your agents"
permalink: /services/agentik/
page_kind: service
service_slug: "agentik"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/agentik.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agentik.md"
tagline: "The tool gateway for your agents"
verified_at: "2026-11-24"
website: "https://www.agentik.cc"
repository: "https://github.com/agent-tool-router/agentik"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT for the SDK, CLI, and Claude Code plugin. The hosted service is closed-source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-24</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.agentik.cc" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.agentik.cc/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agent-tool-router/agentik" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agentik.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agentik is a hosted tool gateway. An agent discovers third-party data and media tools, reads the input schema and the price, then runs the chosen tool against one prepaid workspace balance. The markdown homepage describes one MCP connection for Claude, ChatGPT, Codex, and Cursor, charged at the provider's price. On 2026-11-24 that page listed 3,539 tools from 165 providers.

Discovery and inspection are public. `POST https://api.agentik.cc/v1/discover` returned HTTP 200 on 2026-11-24 for a catalog search and did not call a provider. Running a tool, including a zero-price tool, needs an authorised workspace. The OpenAPI summary is: “Pay-per-call tools for AI agents: one API key, one prepaid balance, many providers.”

The open-source pieces are the CLI, the TypeScript SDK, and the Claude Code plugin. The hosted catalog and billing stay closed.

The published skill also covers the user's own ad and analytics accounts, and webhooks the user creates for Slack, Discord, Zapier, Make, n8n, or Pipedream. Agentik's own comparison says it does not sign in to mail, chat, or CRM apps. Composio and Arcade, already in this category, are the listings for that job.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP. A person must approve OAuth or create an API key, and add prepaid credit before a paid run.
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP. A person must approve OAuth or create an API key, and add prepaid credit before a paid run.

```bash
npx @get-agentik/cli connect <client>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agentik.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://ai.agentik.cc/mcp` (OAuth or `trk_` bearer); `https://ai.agentik.cc/mcp/public` (no key, discover and inspect only) |
| REST / OpenAPI | https://api.agentik.cc/openapi/agent.json version 0.1.0, title “Agentik agent API”. Customer paths include `/v1/discover`, `/v1/tools/{provider}/{tool}`, `/v1/run`, `/v1/runs/{id}`, `/v1/wallet/balance`, and `/v1/topups` |
| CLI | `npx @get-agentik/cli` 0.1.0 (MIT). `connect <client>`, `skill --install` |
| SDK | `npm install @get-agentik/sdk` 0.1.0 (MIT). TypeScript client with OpenAI, Anthropic, and AI SDK adapters |
| Agent Skill | https://www.agentik.cc/SKILL.md and `npx @get-agentik/cli skill --install` |
| Docs | https://www.agentik.cc/docs |

---

## Verification

Last verified **2026-11-24**.

Sources:
- https://www.agentik.cc/index.md
- https://www.agentik.cc/docs
- https://www.agentik.cc/SKILL.md
- https://www.agentik.cc/llms.txt
- https://www.agentik.cc/pricing.md
- https://www.agentik.cc/connect.md
- https://api.agentik.cc/openapi/agent.json
- https://ai.agentik.cc/mcp/public
- https://ai.agentik.cc/mcp
- https://api.agentik.cc/v1/discover
- https://github.com/agent-tool-router/agentik

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
