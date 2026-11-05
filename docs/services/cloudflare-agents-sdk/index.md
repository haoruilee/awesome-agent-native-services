---
title: "Cloudflare Agents SDK | Agent-Native Services"
service_name: "Cloudflare Agents SDK"
description: "Build and host durable AI agents on Cloudflare's global network"
permalink: /services/cloudflare-agents-sdk/
page_kind: service
service_slug: "cloudflare-agents-sdk"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cloudflare-agents-sdk.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-agents-sdk.md"
tagline: "Build and host durable AI agents on Cloudflare's global network"
website: "https://developers.cloudflare.com/agents/"
repository: "https://github.com/cloudflare/agents"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · websocket · CLI · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://developers.cloudflare.com/agents/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://developers.cloudflare.com/agents/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cloudflare/agents" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-agents-sdk.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cloudflare Agents SDK is a runtime for **persistent, stateful agent workloads** on Cloudflare. Each agent session is backed by Durable Objects with durable identity, local SQL storage, WebSocket/SSE communication, scheduling, and recovery. The same platform exposes tools for browser automation, sandboxed code execution, AI Search, MCP tools, and agentic payments.

The 2026 Agents releases expand the runtime with Project Think for long-running agents, sub-agents, durable recovery, Browser Run through a durable `browser_execute` tool, and Code Mode for letting agents write and execute typed code against external tools instead of carrying huge tool-definition prompts.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, websocket, CLI, SDK, http
- **MCP:** ✅ First-class MCP support.
- **Agent Skill:** Unknown
- **Onboarding type:** `cli`

## How agents onboard

```bash
npx create-cloudflare@latest --template cloudflare/agents-starter
cd agents-starter && npm install
npm run dev
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-agents-sdk.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `agents` package / `cloudflare/agents` examples |
| Workers runtime | Durable Objects, Workers bindings, scheduled tasks, WebSockets, SSE |
| MCP | Streamable HTTP servers, MCP clients, `McpAgent`, `McpClient`, `createMcpHandler` |
| Browser automation | Browser Run / Browser Rendering bindings, CDP-oriented tools |
| Code execution | Sandbox tools and Code Mode runtime |
| Observability | Logs, metrics, traces integrated with the Agents runtime |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
