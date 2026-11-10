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
