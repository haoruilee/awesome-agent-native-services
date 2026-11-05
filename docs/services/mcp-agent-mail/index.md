---
title: "MCP Agent Mail | Agent-Native Services"
service_name: "MCP Agent Mail"
description: "Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite"
permalink: /services/mcp-agent-mail/
page_kind: service
service_slug: "mcp-agent-mail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/mcp-agent-mail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail.md"
tagline: "Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite"
website: "https://github.com/Dicklesworthstone/mcp_agent_mail"
repository: "https://github.com/Dicklesworthstone/mcp_agent_mail"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Dicklesworthstone/mcp_agent_mail" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCP Agent Mail provides a mailbox-style coordination layer for coding agents. Agents register persistent identities, exchange structured messages, search threads, and coordinate edits via advisory file reservations. Message artifacts are persisted in Git while query and indexing workloads are handled by SQLite.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Community skills exist, but no official first-party SKILL.md package is published as of April 2026.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
uvx mcp_agent_mail
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mcp-agent-mail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP tools | Message, thread, reservation, and agent lifecycle operations |
| MCP resources | Read-only mailbox, thread, reservation, and diagnostics views |
| CLI | `uvx mcp_agent_mail` startup and ops utilities |
| Git + SQLite | Durable artifact layer + indexed query layer |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
