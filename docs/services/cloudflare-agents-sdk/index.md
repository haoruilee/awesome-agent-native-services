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

<section class="service-essay" aria-label="Editorial" markdown="1">

### Library, platform, or both

The catalog marks the Agent Skill as unknown, even though the dossier prints an install command for an `agents-sdk` skill in the `cloudflare/skills` repository. Treat that as a lead to verify rather than a confirmed bundle. The larger gap is scope. The SDK is open source, but it runs on Workers and Durable Objects in your Cloudflare account, and the dossier lists Browser Run, Sandbox, AI Search, MCP governance, Code Mode, and payments in the same breath without saying which ship in the `agents` package and which are separate Cloudflare products with their own setup and terms. The [Agents docs](https://developers.cloudflare.com/agents/) are where to sort that out.

Operation is therefore shared. Cloudflare runs the runtime; you own the account, the API tokens, and the deployment.

### One Durable Object per agent

What the dossier documents well is the state model. An Agent class is a Durable Object, so each agent instance has a durable identity, its own SQL storage, WebSocket and SSE connections, and scheduled tasks. The runtime recovers from deploys, evictions, and dropped connections, so a long task picks up where it stopped without anyone rebuilding session state. Project Think adds a harness for long-running agents with sub-agents and workflows.

The start command is printed: `npx create-cloudflare@latest --template cloudflare/agents-starter`. The starter includes streaming chat, server-side and client-side tools, human approval, and scheduled tasks.

MCP is first-class in both directions. `McpAgent` and `createMcpHandler` build remote MCP servers over Streamable HTTP, `McpClient` consumes them, and OAuth guides cover authorization. Code Mode lets an agent write typed code against tools instead of carrying long tool definitions in the prompt. It can pause on approval-gated actions and replay completed calls from a durable log once a person approves.

### Next to other runtimes

[Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) mixes several kinds of product. [Letta](/services/letta/) pitches stateful agents in production, which overlaps with the Durable Object model; its dossier is the comparison to read if you want that state without committing to one cloud. [Modal](/services/modal/) describes AI infrastructure for developers, a compute pitch rather than an agent object model. [Cyberdesk](/services/cyberdesk/) provides virtual desktops, a different layer again. The tagline, "Build and host durable AI agents on Cloudflare's global network.", says the important part plainly: the network is the product. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a cloud vendor's SDK qualifies for the list.

### Editor's take

Teams already on Workers, or ones that want per-agent state, scheduling, and remote MCP without running servers, get a lot from this SDK. If your agents must run on another cloud or on hardware you control, it is the wrong dependency, and Letta or Modal are the comparisons to make. These conclusions come from reading the catalog's file and Cloudflare's developer docs; no agent was deployed to reach them.

</section>

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
