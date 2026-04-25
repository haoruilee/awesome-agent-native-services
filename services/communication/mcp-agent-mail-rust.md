# MCP Agent Mail (Rust)

> **"It's like Gmail for your coding agents!"**

| | |
|---|---|
| **Website** | https://github.com/Dicklesworthstone/mcp_agent_mail_rust |
| **Docs** | https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/README.md |
| **GitHub** | https://github.com/Dicklesworthstone/mcp_agent_mail_rust |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://github.com/Dicklesworthstone/mcp_agent_mail_rust

---

## Official Repo

https://github.com/Dicklesworthstone/mcp_agent_mail_rust

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

Install and start the Rust server:

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail_rust/main/install.sh?$(date +%s)" | bash
am
```

This boots the Agent Mail runtime (default local HTTP endpoint) and exposes MCP tools/resources for multi-agent collaboration.

---

## Agent Skills

**Status:** ⚠️ No official first-party `SKILL.md` package published (as of April 2026).

Search community skills:

```bash
npx clawhub@latest search "agent mail"
```

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP server** | Built-in (`am` runtime) |
| **Tools** | 30+ tools (agent registration, messaging, reservations, macros) |
| **Resources** | 20+ read-only resources for inbox/thread/project/tooling state |
| **Client compatibility** | Claude Code, Codex CLI, Gemini CLI, Copilot CLI, and generic MCP clients |

---

## What It Does

MCP Agent Mail (Rust) is a high-performance, production-grade coordination layer for autonomous coding agents. It provides mailbox identities, asynchronous threaded messaging, advisory file leases, and state/resource APIs optimized for concurrent multi-agent software delivery.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README frames the product as coordination infrastructure specifically for coding agents |
| **Agent-specific primitive** | Agent mailboxes + advisory file reservations + MCP macros are primitives tailored to agent swarms |
| **Autonomy-compatible control plane** | Agents can register, communicate, reserve files, and coordinate without per-step human confirmation |
| **M2M integration surface** | MCP tools/resources and CLI runtime are the primary operational interface |
| **Identity / delegation** | Named per-agent identities, per-project scopes, and attributable actions across message/reservation events |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Persistent agent identities** | Stable agent mailbox identities for long-running collaborations |
| **Threaded asynchronous messaging** | Structured messages across multiple cooperating agents |
| **Advisory file reservations** | TTL-based file/glob leases to prevent accidental edit conflicts |
| **Macro tools** | Composite MCP operations for faster small-model coordination loops |
| **Diagnostics/ops surfaces** | TUI + resource views + operational health tools for reliable autonomous execution |

---

## Autonomy Model

1. Agent runtime boots `am` and exposes MCP surface.
2. Each agent registers identity in a project context.
3. Agents coordinate via threads/messages instead of chat-room broadcast.
4. Agents set file reservations before editing and resolve conflicts programmatically.
5. Agents consume MCP resources to recover state after restarts and continue execution.

---

## Identity and Delegation Model

- **Identity:** Named, project-scoped agent identities.
- **Delegation:** Task ownership and message routing occur at agent identity layer.
- **Auditability:** Git-backed artifacts + SQLite index provide traceable history for each action.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP tools | Write/mutate operations for agent, message, reservation lifecycle |
| MCP resources | Read-only views for mailbox, threads, agents, reservations, diagnostics |
| Local HTTP runtime | Default local endpoint for connected clients |
| TUI / robot CLI | Operator and automation interfaces over the same backing state |

---

## Human-in-the-Loop Support

Optional. Humans can inspect/operate through TUI or web views, while autonomous agent loops remain first-class.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic team chat tools** | Not built for autonomous agent identity, MCP-native coordination, or file lease semantics |
| **Plain task boards** | Missing real-time mailbox protocol and per-message tooling contracts for agent loops |
| **Shared branch conventions only** | Do not provide explicit inbox/thread/reservation primitives needed for robust multi-agent concurrency |

---

## Use Cases

- **High-throughput coding swarms** across multiple specialized agents.
- **Reliable agent handoffs** with thread continuity and replayable history.
- **Conflict-aware collaborative editing** in monorepos.
- **Autonomous project execution** with operator visibility and low-overhead recovery.
