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
