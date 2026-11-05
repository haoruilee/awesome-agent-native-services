---
title: "MCP Agent Mail (Rust) | Agent-Native Services"
service_name: "MCP Agent Mail (Rust)"
description: "It's like Gmail for your coding agents!"
permalink: /services/mcp-agent-mail-rust/
page_kind: service
service_slug: "mcp-agent-mail-rust"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/mcp-agent-mail-rust.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail-rust.md"
tagline: "It's like Gmail for your coding agents!"
website: "https://github.com/Dicklesworthstone/mcp_agent_mail_rust"
repository: "https://github.com/Dicklesworthstone/mcp_agent_mail_rust"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail_rust" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail_rust" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail-rust.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCP Agent Mail (Rust) is a high-performance, production-grade coordination layer for autonomous coding agents. It provides mailbox identities, asynchronous threaded messaging, advisory file leases, and state/resource APIs optimized for concurrent multi-agent software delivery.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official first-party SKILL.md package published (as of April 2026).
- **Onboarding type:** `mcp`

## How agents onboard

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail_rust/main/install.sh?$(date +%s)" | bash
am
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail-rust.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP tools | Write/mutate operations for agent, message, reservation lifecycle |
| MCP resources | Read-only views for mailbox, threads, agents, reservations, diagnostics |
| Local HTTP runtime | Default local endpoint for connected clients |
| TUI / robot CLI | Operator and automation interfaces over the same backing state |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
