---
title: "AgentAnycast | Agent-Native Services"
service_name: "AgentAnycast"
description: "Connect AI agents across any network. No public IP required"
permalink: /services/agentanycast/
page_kind: service
service_slug: "agentanycast"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/agentanycast.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentanycast.md"
tagline: "Connect AI agents across any network. No public IP required"
website: "https://github.com/AgentAnycast/agentanycast"
repository: "https://github.com/AgentAnycast/agentanycast"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">SDKs and protocol: Apache-2.0; daemon and relay: FSL-1.1-Apache-2.0 (per repo README license section)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · STDIO</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/AgentAnycast/agentanycast" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/AgentAnycast/agentanycast/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/AgentAnycast/agentanycast" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentanycast.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentAnycast is a **peer-to-peer runtime** for AI agents that need to be reachable without a public URL. The project positions itself as fixing a gap in agent-to-agent protocols that assume every agent exposes a public endpoint: real agents often run on laptops, behind NAT, or inside corporate networks. It provides **NAT traversal** (DCUtR hole punching + relay fallback), **Noise_XX end-to-end encryption**, and **skill-based anycast routing** so peers discover each other by advertised capabilities (`AgentCard` + `Skill` metadata) rather than by DNS or static URLs.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + MCP (stdio via agentanycastd or uvx agentanycast-mcp) + auto-managed daemon
- **Catalog protocols:** MCP, SDK, STDIO
- **MCP:** ✅ Available — MCP is implemented in the Go daemon (agentanycastd); PyPI package agentanycast-mcp wraps it for uvx workflows.
- **Agent Skill:** ⚠️ No standalone npx skills add registry entry — onboarding is README + PyPI/npm + MCP docs above.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK + MCP (stdio via agentanycastd or uvx agentanycast-mcp) + auto-managed daemon

```bash
pip install agentanycast && agentanycast demo
# Second terminal — use the peer id printed by the demo:
agentanycast send <PEER_ID> "Hello!"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentanycast.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install agentanycast` — `Node`, `AgentCard`, `Skill`, `@node.on_task` |
| TypeScript SDK | `npm install agentanycast` |
| MCP | `agentanycastd --mcp-listen stdio` or `uvx agentanycast-mcp` |
| Daemon | `~/.agentanycast/bin/agentanycastd` (auto-installed with Python SDK) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
