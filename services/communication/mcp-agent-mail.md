# MCP Agent Mail

> **"Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite."**

| | |
|---|---|
| **Website** | https://github.com/Dicklesworthstone/mcp_agent_mail |
| **Docs** | https://github.com/Dicklesworthstone/mcp_agent_mail/blob/main/README.md |
| **GitHub** | https://github.com/Dicklesworthstone/mcp_agent_mail |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://github.com/Dicklesworthstone/mcp_agent_mail

---

## Official Repo

https://github.com/Dicklesworthstone/mcp_agent_mail

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

Run Agent Mail via `uvx`:

```bash
uvx mcp_agent_mail
```

Then connect your MCP client (Claude Code/Codex/Gemini CLI, etc.) to the Agent Mail server and use tools such as `register_agent`, `send_message`, `fetch_inbox`, and `file_reservation_paths`.

---

## Agent Skills

**Status:** ⚠️ Community skills exist, but no official first-party `SKILL.md` package is published as of April 2026.

Search available skills:

```bash
npx clawhub@latest search mcp_agent_mail
```

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Transport** | HTTP and stdio (via MCP-compatible wrappers/clients) |
| **Server package** | `mcp_agent_mail` |
| **Primary tools** | Agent registration, inbox/outbox operations, threaded messaging, advisory file reservations |
| **Resources** | Read-only mailbox/thread/project resources for low-cost state reads |

---

## What It Does

MCP Agent Mail provides a mailbox-style coordination layer for coding agents. Agents register persistent identities, exchange structured messages, search threads, and coordinate edits via advisory file reservations. Message artifacts are persisted in Git while query and indexing workloads are handled by SQLite.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Project README explicitly positions the system as a coordination layer for AI coding agents |
| **Agent-specific primitive** | `register_agent`, inbox/outbox workflows, and file-reservation leases are built for autonomous multi-agent collaboration |
| **Autonomy-compatible control plane** | Agents can self-register, message peers, and reserve files without human approvals per action |
| **M2M integration surface** | MCP tools/resources and CLI-driven API surface are the primary interface |
| **Identity / delegation** | Per-agent identities, per-project scopes, and attributable message/reservation history |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent identity registration** | Register persistent per-agent identity within a project scope |
| **Inbox/outbox messaging** | Send, receive, acknowledge, and search structured agent messages |
| **Threading** | Keep asynchronous multi-step work grouped by thread |
| **File reservations** | Advisory leases on files/globs to reduce multi-agent edit collisions |
| **Git-backed artifacts** | Durable, human-auditable message/reservation history |

---

## Autonomy Model

1. Agent starts or connects to Agent Mail MCP server.
2. Agent calls registration tools to create/restore identity in the target repo/project.
3. Agent coordinates work through inbox/outbox and thread tools.
4. Agent acquires advisory file reservations before edits and releases/renews as needed.
5. Agent continues autonomous collaboration using mailbox state + MCP resources.

---

## Identity and Delegation Model

- **Identity:** Each agent gets a named identity (`agent_name`) within a project scope.
- **Delegation:** Agents operate under project-level delegation boundaries and tool-level permissions.
- **Audit:** Message traffic and reservations are persisted with attribution for replay and debugging.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP tools | Message, thread, reservation, and agent lifecycle operations |
| MCP resources | Read-only mailbox, thread, reservation, and diagnostics views |
| CLI | `uvx mcp_agent_mail` startup and ops utilities |
| Git + SQLite | Durable artifact layer + indexed query layer |

---

## Human-in-the-Loop Support

Optional. Human operators can inspect mailbox artifacts and intervene, but the core coordination loop is autonomous and agent-to-agent.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Slack/Discord bots** | Human-centric channels, weak agent identity semantics, and no first-class file-reservation coordination primitives |
| **Ad-hoc shared docs/issues** | Lacks structured MCP tools/resources for deterministic autonomous workflows |
| **Raw Git commits only** | No inbox/outbox semantics, thread-level coordination, or lease-based collision reduction |

---

## Use Cases

- **Parallel coding swarms** coordinating backend/frontend/infra agents.
- **Cross-agent handoff workflows** where one agent delegates and another executes.
- **Conflict-aware editing** with advisory file reservations.
- **Long-running autonomous projects** requiring durable asynchronous communication.
