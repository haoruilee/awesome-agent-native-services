# Claude Peers (claude-peers-mcp)

> **"Allow all your Claude Codes to message each other ad-hoc!"**

| | |
|---|---|
| **Website** | https://github.com/louislva/claude-peers-mcp |
| **Docs** | https://github.com/louislva/claude-peers-mcp/blob/main/README.md |
| **GitHub** | https://github.com/louislva/claude-peers-mcp |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://github.com/louislva/claude-peers-mcp

---

## Official Repo

https://github.com/louislva/claude-peers-mcp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP (stdio) + local broker`

```bash
git clone https://github.com/louislva/claude-peers-mcp.git ~/claude-peers-mcp
cd ~/claude-peers-mcp
bun install

# Register the MCP server for Claude Code (user scope)
claude mcp add --scope user --transport stdio claude-peers -- bun ~/claude-peers-mcp/server.ts

# Run Claude Code with the claude-peers development channel
claude --dangerously-skip-permissions --dangerously-load-development-channels server:claude-peers
```

Requires [Bun](https://bun.sh), Claude Code v2.1.80+, and claude.ai login (channels). See [README](https://github.com/louislva/claude-peers-mcp/blob/main/README.md) for CLI (`bun cli.ts peers`, `send`, `status`) and environment variables (`CLAUDE_PEERS_PORT`, `CLAUDE_PEERS_DB`, optional `OPENAI_API_KEY` for auto-summary).

---

## Agent Skills

**Status:** ⚠️ Not published — onboarding is via repo README and MCP registration.

---

## MCP

**Status:** ✅ Primary interface — stdio MCP server (`server.ts`) exposing peer discovery and messaging tools.

| Tool | Description |
|---|---|
| `list_peers` | Discover other Claude Code instances (scope: `machine`, `directory`, or `repo`) |
| `send_message` | Send a message to another instance by ID (push via Claude Code channels when enabled) |
| `set_summary` | Set a visible summary of what this session is working on |
| `check_messages` | Poll for inbound messages (fallback without channel push) |

---

## What It Does

Claude Peers runs a **localhost broker** (default port `7899`, SQLite-backed) so multiple **Claude Code** sessions on the same machine can discover each other and exchange messages in real time. Each session runs an MCP server that registers with the broker; inbound messages can be delivered instantly through the [Claude Code channels](https://code.claude.com/docs/en/channels-reference) protocol. Traffic stays **local** — no cloud relay for peer messaging.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo description: *"Allow all your Claude Codes to message each other ad-hoc!"*; README: *"Let your Claude Code instances find each other and talk"* — [GitHub](https://github.com/louislva/claude-peers-mcp), [README](https://raw.githubusercontent.com/louislva/claude-peers-mcp/main/README.md) |
| **Agent-specific primitive** | `list_peers` / `send_message` scoped to other **agent sessions** (cwd, git repo, machine); `set_summary` for cross-session situational awareness — not a human inbox or generic chat API |
| **Autonomy-compatible control plane** | Agents call MCP tools without per-message human approval; broker auto-starts and cleans dead peers |
| **M2M integration surface** | MCP stdio server + optional CLI (`cli.ts`); configuration via env vars |
| **Identity / delegation** | Each registered session has a **peer ID**; messages are addressed to a specific peer; SQLite + broker state give a attributable session registry on the machine |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Local broker daemon** | `localhost:7899` + SQLite (`~/.claude-peers.db` by default) |
| **Peer discovery** | `list_peers` with machine / directory / repo scope |
| **Ad-hoc agent messaging** | `send_message` to peer ID with channel push or poll fallback |
| **Session summary** | Auto-summary via optional `OPENAI_API_KEY`, or `set_summary` tool |
| **CLI inspection** | `bun cli.ts status | peers | send | kill-broker` |

---

## Autonomy Model

```
Claude Code session A starts with claude-peers MCP + development channel
    ↓
MCP server registers with local broker (SQLite)
    ↓
Session B starts the same way
    ↓
Either session calls list_peers → sees peer IDs, cwd, repo, summary
    ↓
send_message(peer_id, ...) → broker routes → channel push to recipient session
    ↓
Recipient agent receives message in context without human relay
```

---

## Identity and Delegation Model

- **Peer identity:** Each live Claude Code session registers as a peer with a broker-assigned identity used for `send_message` targeting.
- **Scope:** Discovery can be limited to same machine, same directory, or same git repository — constraining which agents can see each other.
- **Attribution:** Messages are routed broker-to-peer; CLI can inject messages into a session for debugging (`bun cli.ts send`).
- **Local trust boundary:** All traffic is localhost-only; this is coordination across **your** agent sessions, not a public network.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | stdio — `server.ts` (register via `claude mcp add`) |
| Broker | HTTP on configurable port (default `7899`) |
| Channels | Claude Code `server:claude-peers` development channel for push delivery |
| CLI | `bun cli.ts` — operational commands |

---

## Human-in-the-Loop Support

Not required for peer messaging. A human may run multiple terminals; each Claude instance operates autonomously within its session. Optional: human uses CLI to inspect or send test messages.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Slack / email / shared doc** | Human-centric channels; no peer discovery for **Claude Code sessions** or MCP tool surface |
| **Generic MCP broadcast** | No broker, no peer registry, no repo/directory-scoped discovery, no Claude channel push integration |
| **Plain files / git notes** | Polling and merge friction; not instant session-to-session delivery with agent-oriented tools |

---

## Use Cases

- **Multi-repo coordination** — one Claude session asks another what it is editing before changing shared interfaces
- **Parallel tasks** — several agents on the same machine share short status summaries via `list_peers`
- **Local swarm debugging** — inspect all live Claude Code peers from CLI or any connected session
