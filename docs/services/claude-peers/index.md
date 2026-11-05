---
title: "Claude Peers (claude-peers-mcp) | Agent-Native Services"
service_name: "Claude Peers (claude-peers-mcp)"
description: "Allow all your Claude Codes to message each other ad-hoc!"
permalink: /services/claude-peers/
page_kind: service
service_slug: "claude-peers"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/claude-peers.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-peers.md"
tagline: "Allow all your Claude Codes to message each other ad-hoc!"
website: "https://github.com/louislva/claude-peers-mcp"
repository: "https://github.com/louislva/claude-peers-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/louislva/claude-peers-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/louislva/claude-peers-mcp/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/louislva/claude-peers-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-peers.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Claude Peers runs a **localhost broker** (default port `7899`, SQLite-backed) so multiple **Claude Code** sessions on the same machine can discover each other and exchange messages in real time. Each session runs an MCP server that registers with the broker; inbound messages can be delivered instantly through the [Claude Code channels](https://code.claude.com/docs/en/channels-reference) protocol. Traffic stays **local** — no cloud relay for peer messaging.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (stdio) + local broker
- **Catalog protocols:** MCP, CLI, STDIO, http
- **MCP:** ✅ Primary interface — stdio MCP server (server.ts) exposing peer discovery and messaging tools.
- **Agent Skill:** ⚠️ Not published — onboarding is via repo README and MCP registration.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (stdio) + local broker

```bash
git clone https://github.com/louislva/claude-peers-mcp.git ~/claude-peers-mcp
cd ~/claude-peers-mcp
bun install

# Register the MCP server for Claude Code (user scope)
claude mcp add --scope user --transport stdio claude-peers -- bun ~/claude-peers-mcp/server.ts

# Run Claude Code with the claude-peers development channel
claude --dangerously-skip-permissions --dangerously-load-development-channels server:claude-peers
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-peers.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | stdio — `server.ts` (register via `claude mcp add`) |
| Broker | HTTP on configurable port (default `7899`) |
| Channels | Claude Code `server:claude-peers` development channel for push delivery |
| CLI | `bun cli.ts` — operational commands |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
