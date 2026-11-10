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

<section class="service-essay" aria-label="Editorial" markdown="1">

[MCP Agent Mail](/services/mcp-agent-mail/) and this Rust project come from the same GitHub account and share a coordination model: identities, inboxes, threads, and file leases for coding agents. This listing is the Rust runtime, started with a single command named `am`, with an operator TUI alongside the MCP surface.

### Inboxes without SMTP

Despite the tagline's comparison to Gmail, nothing here sends email to people. The dossier describes a coordination layer for autonomous coding agents working in the same project. Each agent registers a persistent, project-scoped mailbox identity. Agents exchange asynchronous, threaded messages instead of broadcasting into a shared chat. Before editing, an agent takes an advisory reservation on a file or glob, with a time-to-live, so a second agent can see the claim and avoid a collision.

Two more primitives distinguish this version in the dossier. Macro tools bundle several MCP operations into one call, aimed at faster coordination loops with small models. Diagnostics surfaces, a TUI, resource views, and health tools, let an operator see what the swarm is doing. History is stored as Git-backed artifacts with a SQLite index, which the dossier presents as the audit trail.

### Booting the runtime

The README's install path is a shell script fetched with `curl` and piped to `bash`, followed by `am`. That starts a local HTTP endpoint and exposes MCP tools for writes (registration, messages, reservations) and MCP resources for read-only views of inboxes, threads, agents, reservations, and diagnostics. Agents recovering from a restart read those resources to rebuild their state. The README names Claude Code, Codex CLI, Gemini CLI, and Copilot CLI as clients. The dossier gives tool and resource counts; the current set is in the [README](https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/README.md).

No first-party Agent Skill is published. The dossier suggests community search.

### Checks before a swarm depends on it

Read the install script before running it, as with any pipe-to-shell installer. Find out who can reach the local HTTP endpoint and whether it has any authentication; the dossier does not say. Reservations are advisory, so an agent that ignores them is not stopped, and your prompts or harness need to make agents check. If you already run the Python project, the dossier does not say whether its stored data carries over to this runtime.

### Editor's take

Choose the Rust runtime when several coding agents share one repository, you want the macro tools for smaller models, and a terminal dashboard for the operator matters. Teams already settled on the Python project have less reason to switch. If the agents need to correspond with humans over real email, the [Communication](/categories/communication/) category has address-based services such as [MailboxKit](/services/mailboxkit/) and [OpenMail](/services/openmail/), and the [email API guide](/guides/choose-an-email-api-for-agents/) compares them. This opinion was formed from the README and the catalog entry; no agents have been coordinated through `am` for it.

</section>

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
