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

<section class="service-essay" aria-label="Editorial" markdown="1">

[MCP Agent Mail (Rust)](/services/mcp-agent-mail-rust/) is a separate runtime from the same GitHub account, described in its dossier as a production-grade coordination layer tuned for concurrent multi-agent delivery. This listing is the Python project, started with `uvx mcp_agent_mail`, built on FastMCP with Git for durable storage and SQLite for search.

### Messages that land in Git

The dossier describes a mailbox-style coordination layer for coding agents sharing a project. An agent registers a persistent identity, recorded as an `agent_name` within a project scope. It sends, receives, acknowledges, and searches structured messages, grouped into threads so a multi-step handoff stays together. Before editing, it takes an advisory reservation on a file or glob so other agents can see the claim and work elsewhere.

The storage split is the design choice to notice. Message artifacts and reservations persist in Git, which the dossier calls durable and human-auditable. SQLite handles indexing and queries. The practical result is a coordination history that a human can inspect with the same tools used for code, and that an agent can replay after a restart.

### Tools named in the dossier

After starting the server, an MCP client such as Claude Code, Codex, or Gemini CLI connects to it. The dossier names `register_agent`, `send_message`, `fetch_inbox`, and `file_reservation_paths` as example tools. Read-only MCP resources expose mailbox, thread, reservation, and project state for cheap reads. Transport is HTTP, or stdio through MCP-compatible wrappers. The [README](https://github.com/Dicklesworthstone/mcp_agent_mail/blob/main/README.md) is the reference.

No first-party Agent Skill is published as of the dossier's April 2026 check. Community skills exist, and the dossier points to search.

### Python and Rust variants, and real mail

Despite the name, this is not email. The [Communication](/categories/communication/) category also holds address-based services such as [MailboxKit](/services/mailboxkit/) and [OpenMail](/services/openmail/), which put agents on the public mail network to reach people. [Chimely](/services/chimely/) is an in-app notification inbox. Agent Mail stays inside one project's agent swarm. The [email API guide](/guides/choose-an-email-api-for-agents/) covers the address-based choices if that is what you need.

Between the two Agent Mail listings, the primitives overlap: identities, threaded messages, and file leases. Pick by language and tooling preference, and check each README for current features rather than assuming parity.

Questions to settle first: where the Git repository for message artifacts lives, and whether it sits inside your code repository or beside it. Whether the HTTP server has authentication, and who on the network can reach it. Reservations are advisory, so an agent that skips the check is not blocked; the harness or prompt has to enforce the habit.

### Editor's take

The Python project is a sensible default for teams already running Python tooling with `uvx` who want several coding agents to stop overwriting each other and to leave a record they can audit. Operators who would rather run a Rust binary should compare the Rust runtime. Teams whose agents need to write to humans should use a real mail service instead. This view was assembled from the README and the catalog entry; the server has not been started under any of this project's agents.

</section>

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
