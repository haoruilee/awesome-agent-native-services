# agentmemory

> **"Your coding agent remembers everything. No more re-explaining."**

| | |
|---|---|
| **Website** | https://agent-memory.dev |
| **Docs** | https://github.com/rohitg00/agentmemory#readme |
| **GitHub** | https://github.com/rohitg00/agentmemory |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/rohitg00/agentmemory?style=social)](https://github.com/rohitg00/agentmemory) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | [v0.9.29](https://github.com/rohitg00/agentmemory/releases/tag/v0.9.29) released 2026-08-16 (npm `@agentmemory/agentmemory` and `@agentmemory/mcp` 0.9.29); last GitHub push 2026-09-28; 29,029 stars; Apache-2.0 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://agent-memory.dev

---

## Official Repo

https://github.com/rohitg00/agentmemory

---

## ⭐ How to Use (Agent Onboarding)

**Interaction pattern:** `URL Onboarding` ⭐ + local memory server + MCP + Skills

Official README one-instruction path for a coding agent:

```text
Retrieve and follow the instructions at: https://raw.githubusercontent.com/rohitg00/agentmemory/main/INSTALL_FOR_AGENTS.md
```

Direct install:

```bash
npx @agentmemory/agentmemory
agentmemory demo --serve
npx skills add rohitg00/agentmemory -y
```

The first run starts the memory server (default `:3111`). `agentmemory connect <agent>` wires additional hosts. Health check documented as `curl http://localhost:3111/agentmemory/health`.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add rohitg00/agentmemory -y
```

The README documents 17 skills: 9 invocable (`remember`, `recall`, `recap`, `handoff`, `forget`, `lesson`, `commit-context`, `commit-history`, `session-history`) and 8 reference skills (discipline, MCP tools, REST, config, agents, hooks, architecture, skill-authoring).

Claude Code can also `/plugin marketplace add rohitg00/agentmemory` then `/plugin install agentmemory`.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/rohitg00/agentmemory (`@agentmemory/mcp`) |
| **Transport** | stdio proxy to the local (or remote) memory server |
| **Compatible Clients** | Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes, OpenCode, Cline, Goose, and any MCP client |

README: plugin path auto-wires `@agentmemory/mcp` with on the order of 54 tools when the server is up (`memory_smart_search`, `memory_save`, `memory_sessions`, `memory_governance_delete`, and others). Without a reachable server the shim falls back to a smaller local tool set.

---

## What It Does

agentmemory is a local-first persistent memory layer for coding agents. One memory server is shared across Claude Code, Codex, Cursor, and other MCP clients. It extends an LLM-wiki style store with confidence, lifecycle, knowledge graphs, and hybrid search (built on a pinned iii-engine). Agents save, recall, hand off, and forget through hooks, MCP, REST, and skills instead of re-pasting project lore every session.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Your coding agent remembers everything. No more re-explaining."** / **"Persistent memory for Claude Code, GitHub Copilot CLI, Cursor, … and any MCP client."** — [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) |
| **Agent-specific primitive** | Shared memory server with smart search, session memory, governance delete, handoff, and hook-injected recall — not a generic vector DB API |
| **Autonomy-compatible control plane** | After install, hooks and MCP run without a human choosing what to embed each turn |
| **M2M integration surface** | INSTALL_FOR_AGENTS.md URL, CLI, REST on `:3111`, `@agentmemory/mcp`, Skills, plugins |
| **Identity / delegation** | Memories are scoped through the memory server and agent adapters; governance delete and leases/signals are documented. Optional `AGENTMEMORY_URL` + `AGENTMEMORY_SECRET` for protected/remote deployments |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Memory server** | Local HTTP service (default `:3111`) shared by all wired agents |
| **Smart search / save** | MCP/REST recall and persist |
| **Lifecycle hooks** | Host-specific observe/inject so recall happens without a prompt |
| **Handoff / lesson** | Explicit skills for transferring or extracting durable notes |
| **Governance delete** | Controlled forgetting |
| **Viewer** | Optional local UI (README mentions `:3113`) |

---

## Autonomy Model

```
Agent follows INSTALL_FOR_AGENTS.md or npx @agentmemory/agentmemory
    -> memory server starts
    -> connect / plugin / MCP wires the host
    -> hooks capture and inject memory across turns
    -> agent calls recall/remember via MCP or skills
    -> memories persist across sessions
```

---

## Identity and Delegation Model

- **Shared store:** One server, many agent adapters.
- **Remote lock:** `AGENTMEMORY_URL` and `AGENTMEMORY_SECRET` for protected deployments.
- **Governance:** Dedicated delete/governance tools rather than silent overwrite-only.
- **No cloud user OAuth product:** Default is local; Windows native connect is documented as limited (WSL2 preferred).
- **Engine pin:** Ships a pinned iii-engine; will not attach to a mismatched local `iii`.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `npx @agentmemory/agentmemory`, `agentmemory connect`, `demo` |
| REST | `http://localhost:3111` |
| MCP | `@agentmemory/mcp` stdio |
| Skills | `npx skills add rohitg00/agentmemory -y` |
| Onboarding URL | `INSTALL_FOR_AGENTS.md` |

---

## Human-in-the-Loop Support

First-run installer can be interactive (pick agents and an LLM provider, or stay keyless). After that, memory I/O is autonomous. Governance delete is an explicit agent/operator action.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw vector database** | Agent must decide extract/update/evict; no coding-agent hooks or shared MCP tool surface |
| **Chat product memory** | Locked to one vendor chat UI |
| **Notes file in the repo** | No hybrid search, lifecycle, or cross-harness server |

---

## Use Cases

- **Stop re-explaining** a codebase's conventions every session
- **Handoff** between Claude Code and Codex on the same memory server
- **Lesson extraction** after a debugging arc
- **Remote/protected memory** with URL + secret
