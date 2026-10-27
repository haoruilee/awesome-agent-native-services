# ContextStream

> **"Persistent memory. Millisecond code search."**

| | |
|---|---|
| **Website** | https://contextstream.io |
| **Docs** | https://contextstream.io/docs · https://contextstream.io/docs/editors/setup · https://contextstream.io/llms.txt |
| **GitHub** | https://github.com/contextstream/mcp-server |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/contextstream/mcp-server?style=social)](https://github.com/contextstream/mcp-server) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Verified at** | 2026-10-27 |
| **Latest-month signal** | Hosted MCP and docs return HTTP 200; [contextstream/mcp-server](https://github.com/contextstream/mcp-server) last push 2026-10-27; install scripts at `contextstream.io/scripts/mcp.sh` and `mcp.ps1` |

---

## Official Website

https://contextstream.io

---

## Official Repo

https://github.com/contextstream/mcp-server — open-source MCP server (local install + hosted gateway). Official MCP Registry name: `io.contextstream/mcp`.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP install script / hosted MCP

**Quickest verified path (macOS/Linux):**

```bash
curl -fsSL https://contextstream.io/scripts/mcp.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://contextstream.io/scripts/mcp.ps1 | iex
```

Hosted MCP (after account/workspace): `https://mcp.contextstream.io/mcp?default_context_mode=fast`

Editor setup: https://contextstream.io/docs/editors/setup

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills bundle located in verified materials; primary path is the MCP install scripts / hosted MCP.

---

---

## MCP

**Status:** ✅ Official MCP server (local + hosted)

| Detail | Value |
|---|---|
| **Repo** | https://github.com/contextstream/mcp-server |
| **Hosted** | https://mcp.contextstream.io/mcp |
| **Transport** | stdio (local) / Streamable HTTP (hosted) |
| **Auth** | Sign-in during MCP onboarding; workspace-scoped access |
| **Clients** | Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI, and other MCP clients |

Optional Slipstream agents surface as an MCP tool when enabled on a workspace (credit-priced specialist runs).

---

## What It Does

ContextStream gives coding agents **shared project context**: hybrid code search over indexed project files plus saved decisions, lessons, plans, and related memory that travel across sessions and tools. Indexing supplies code context; agents are expected to save decisions explicitly so later sessions can retrieve them.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product and MCP README target AI coding agents as primary clients |
| **Agent-specific primitive** | Persistent cross-session project memory + code search for agent loops; Slipstream specialist agents invoked from the same MCP surface |
| **M2M surface** | Official MCP server (local install scripts and hosted gateway) |
| **Scoped access** | Workspace-scoped indexing and controls documented in data-handling / privacy docs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Project code search** | Hybrid semantic/keyword search over indexed eligible project files |
| **Saved decisions / lessons / plans** | Cross-session memory agents write and retrieve explicitly |
| **Hosted + local MCP** | Same product surface via install script or `mcp.contextstream.io` |
| **Slipstream agents** | Optional credit-priced specialist agents invoked from MCP when enabled |

---

## Autonomy Model

```
Agent connects via MCP (local script or hosted URL)
    ↓
Indexes / searches project files; retrieves saved decisions and lessons
    ↓
Agent saves new decisions/lessons for later sessions
    ↓
(Optional) Slipstream tool hands a bounded job to a specialist agent in the same workspace
```

Humans configure workspace/privacy settings; day-to-day recall and search run inside the agent loop.

---

## Identity and Delegation Model

- Access is **workspace-scoped** after MCP onboarding / sign-in.
- Hosted connections can name a workspace via `X-ContextStream-Workspace-Id`.
- Slipstream auto-accept caps (credits) are set by the operator in the local MCP env or hosted headers — agents cannot raise caps above what the operator configured.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (local) | `curl …/scripts/mcp.sh \| bash` or PowerShell `mcp.ps1` |
| MCP (hosted) | `https://mcp.contextstream.io/mcp` |
| Docs / llms.txt | https://contextstream.io/docs · https://contextstream.io/llms.txt |
| Benchmarks | https://contextstream.io/benchmarks |

---

## Human-in-the-Loop Support

Humans create/sign into the workspace and set privacy/indexing controls. Day-to-day search, recall, and (optional) Slipstream runs happen inside the agent loop. Slipstream priced runs can require acceptance unless an auto-accept credit cap is set by the operator.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain vector DB / notes file** | No agent-oriented MCP onboarding, decision lifecycle, or cross-tool workspace memory productized for coding agents |
| **Generic code search SaaS** | Not built as persistent agent memory with saved decisions across MCP clients |
| **Chat transcript alone** | Does not index the repo or carry structured decisions across tools |

---

## Use Cases

- Keep architectural decisions and lessons available across Cursor / Claude Code / Codex sessions
- Find relevant files before a change and cite saved project context
- Hand bounded jobs (PR review, release notes) to Slipstream specialists in the same workspace

---

## Verification Sources

- https://github.com/contextstream/mcp-server (MIT, push 2026-10-27)
- https://contextstream.io/docs/editors/setup (HTTP 200)
- https://contextstream.io/llms.txt (HTTP 200)
