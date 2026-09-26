# Toolport

> **"Every tool. One port."**

| | |
|---|---|
| **Website** | https://toolport.app |
| **Docs** | https://github.com/btsouth/toolport#readme |
| **GitHub** | https://github.com/btsouth/toolport |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/btsouth/toolport?style=social)](https://github.com/btsouth/toolport) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Repository transferred from `tsouth89/toolport` to `btsouth/toolport` (old URL redirects); last push 2026-09-26; license MIT ([repo metadata](https://api.github.com/repos/btsouth/toolport)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://toolport.app

---

## Official Repo

https://github.com/btsouth/toolport

Transferred from `tsouth89/toolport`; the old URL redirects here (confirmed 2026-09-26). Live GitHub description: **“Local-first MCP gateway. One port for every tool and every AI client: lazy discovery (~90% token savings), tool integrity + quarantine, secrets in the OS keychain.”** License MIT. Last push 2026-09-26.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `local MCP gateway` (stdio) after a one-time desktop install

1. Download the installer from https://github.com/btsouth/toolport/releases/latest
2. Add MCP servers in the app (catalog, MCP Registry, or pasted client snippets)
3. Connect each AI client so it launches `toolport-gateway` over stdio

Once connected, the agent talks only to Toolport. In lazy-discovery mode it sees compact meta-tools instead of every downstream schema:

- `toolport_status`
- `toolport_search_tools`
- `toolport_call_tool`
- `toolport_fetch_result`

Optional tools appear when the matching feature is on (`toolport_confirm`, enable/disable, `toolport_run_script`, saved routines).

---

## Agent Skills

**Status:** ⚠️ Not published as a `SKILL.md` package

Toolport can write a marked block into each client's agent-rules file (`AGENTS.md`, `GEMINI.md`, and similar). That is host rules sync, not an Agent Skills package.

Search community skills: `npx clawhub@latest search toolport`. See: https://agentskills.io/specification

---

## MCP

**Status:** ✅ Available (gateway)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/btsouth/toolport |
| **Transport** | stdio (`toolport-gateway`); downstream servers may be stdio or remote HTTP/SSE |
| **Compatible Clients** | Official README lists auto-detect/connect for 34 clients including Claude Desktop, Claude Code, Cursor, VS Code, Codex, Gemini CLI, Windsurf, OpenCode, and others |

Toolport is the MCP front door: clients do not load every downstream tool into context.

---

## What It Does

Toolport is a local-first MCP gateway. A human (or installer) authenticates each server once. Every AI client then points at one gateway and shares that catalog. Lazy discovery replaces thousands of tool-definition tokens with a handful of meta-tools the agent searches on demand. The same path fingerprints tool schemas (rug-pull / poisoning), marks untrusted returned content, and can pause destructive calls for human approval.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"One local gateway for all your MCP servers, shared by every AI client"** and **"Every tool. One port."** — [repo](https://github.com/btsouth/toolport) |
| **Agent-specific primitive** | Lazy-discovery meta-tools (`toolport_search_tools` / `toolport_call_tool`) plus per-client server profiles so a coding agent cannot see a billing server |
| **Autonomy-compatible control plane** | After connect, the agent searches and calls tools without a human picking each server. Approval mode is optional and only pauses configured destructive calls |
| **M2M integration surface** | `toolport-gateway` stdio MCP is what every client launches |
| **Identity / delegation** | Per-agent/client profiles scope which servers exist. Secrets stay in the OS keychain and are never written into client MCP configs |

This is not a duplicate of ToolHive or IBM MCP Gateway: those emphasize isolated hosting or federated production gateways. Toolport's catalog-quality primitive is lazy discovery and token-bounded tool access on the local path.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Lazy meta-tools** | Four compact tools replace the full downstream catalog in context |
| **Per-agent profiles** | Each client only sees assigned servers |
| **Tool integrity** | Fingerprints detect silent schema changes and injection-like descriptions |
| **Content defense** | Flags injection-like *returned* content as external data |
| **Approval gate** | Optional pause on destructive calls; deny returns a declined tool call |
| **Routines** | Promote a proven Code Mode run to a saved, schema-checked tool |

---

## Autonomy Model

```
Operator installs Toolport and authenticates servers once
    -> connect each AI client to toolport-gateway
    -> agent calls toolport_search_tools, then toolport_call_tool
    -> gateway routes to the namespaced downstream tool
    -> optional approval card for destructive calls
    -> audit log records latency and errors per server
```

---

## Identity and Delegation Model

- **Client profile:** Each AI client is a scoped view of the registry.
- **Secrets:** OS keychain only; clients never receive downstream API keys.
- **Namespaced tools:** Downstream names become `server__tool` to avoid collisions.
- **No minted agent passport:** Identity is the local client profile plus the gateway audit log.
- **Agent control of servers:** `toolport_enable_server` / `toolport_disable_server` are off by default.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Desktop app | Tauri app for servers, profiles, credentials, clients |
| Gateway | `toolport-gateway` stdio MCP |
| Downstream | stdio or remote HTTP/SSE MCP servers |
| Agent rules sync | Marked blocks in `AGENTS.md` and similar |

---

## Human-in-the-Loop Support

Optional approval mode pauses destructive calls until the operator approves or denies in the app (OS notification when waiting). Deny blocks the call. Routine promotion also requires a one-shot desktop approval card. The gateway itself does not require a click for ordinary allowed tools.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Per-client MCP config** | Repeats auth and dumps every tool schema into every request |
| **Generic HTTP proxy** | No lazy discovery, tool integrity, or per-agent server profiles |
| **Host-only MCP catalog UI** | A human picker is not a runtime search/call plane for the agent |

---

## Use Cases

- **Many MCP servers, one context budget** — keep tool definitions flat
- **One auth, many coding agents** — share Stripe/GitHub/etc. across Cursor, Claude, Codex
- **Scoped agents** — hide billing tools from a coding profile
- **Local supply-chain checks** — flag rug-pulls and poisoned tool text before a call
