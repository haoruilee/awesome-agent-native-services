# Serena

> **"Serena is the IDE for your coding agent."**

| | |
|---|---|
| **Website** | https://oraios.github.io/serena/ |
| **Docs** | https://oraios.github.io/serena/ |
| **GitHub** | https://github.com/oraios/serena |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/oraios/serena?style=social)](https://github.com/oraios/serena) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT |

---

## Official Website

https://oraios.github.io/serena/

---

## Official Repo

https://github.com/oraios/serena

---

## How to Use (Agent Onboarding)

**Install with uv** (recommended upstream path):

```bash
uv tool install -p 3.13 serena-agent@latest --prerelease=allow
serena init
```

Then **configure your MCP client** with a launch command for `serena` — see [Client configuration](https://oraios.github.io/serena/02-usage/030_clients.html) for Claude Code, Codex, Cursor, JetBrains, Claude Desktop, and others.

**Note:** Upstream warns **not to install via unofficial MCP marketplaces** (outdated commands) — follow the [Quick Start](https://github.com/oraios/serena#quick-start) in the official repo.

**JetBrains backend** (optional): `serena init -b JetBrains` — [plugin docs](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html).

---

## Agent Skills

**Status:** ⚠️ Not yet published as a standalone `npx skills add …` pack

Search community skills: `npx clawhub@latest search serena-agent`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Serena is an MCP server (stdio by default; HTTP mode documented)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/oraios/serena |
| **Transport** | stdio (typical) · HTTP mode optional |
| **Compatible Clients** | Claude Code, Codex, OpenCode, Gemini CLI, Cursor, VS Code–based assistants, Claude Desktop, OpenWebUI, etc. — [clients doc](https://oraios.github.io/serena/02-usage/030_clients.html) |

---

## What It Does

Serena gives coding agents **semantic code intelligence**: symbol-level retrieval, editing, and refactoring tools backed by **language servers (LSP)** or an optional **JetBrains plugin**, all exposed through **MCP**. README positions **agent-first tool design** with high-level abstractions instead of brittle line-number grep/replace, plus an optional **memory system** for long-lived agent workflows across large codebases.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Tagline: *"Serena is the **IDE for your coding agent**"*; README describes *"**agent-first tool design**"* and integrates via MCP for LLM clients — [GitHub](https://github.com/oraios/serena) |
| **Agent-specific primitive** | **Symbol-scoped MCP tools** (find symbol, references, rename, structured edits) — abstractions that mirror IDE semantics for **tool-using LLMs**, not a human clicking an IDE |
| **Autonomy-compatible control plane** | After `serena init` and MCP wiring, agents drive edits and navigation without per-keystroke human confirmation |
| **M2M integration surface** | MCP server, `uv`-distributed CLI, optional HTTP mode |
| **Identity / delegation** | Operates on the **developer's workspace** with OS/user file permissions; optional JetBrains backend uses the IDE's analysis process under the developer's account |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Semantic retrieval** | Symbols, references, outlines, type hierarchies (capability matrix varies by LSP vs JetBrains) |
| **Refactoring tools** | Rename/move (per capability table in README) |
| **LSP integration** | 40+ languages via pluggable language servers |
| **JetBrains backend** | Full-IDE analysis via marketplace plugin (paid; trial) |
| **Agent memory** | Long-lived workflow memory (see README "memory system") |
| **Multi-layer config** | Project-scoped tuning for agent behavior |

---

## Autonomy Model

```
Developer runs serena init and adds MCP launch command to the agent host
  ↓
Agent issues MCP tools (symbol search, edit, refactor, …)
  ↓
Serena consults LSP or JetBrains backend
  ↓
Structured results/edits return to the agent for the next reasoning step
```

---

## Identity and Delegation Model

- **Workspace-scoped** — tools act on files the developer's environment can access.
- **No third-party cloud agent identity** — analysis runs locally (LSP subprocesses) or in the developer's JetBrains IDE.
- **Audit** — file changes are normal git-tracked edits attributable to the developer session running the agent.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | Primary integration for coding agents |
| **CLI** | `serena` via `uv tool install … serena-agent` |
| **Docs** | https://oraios.github.io/serena/ |

---

## Human-in-the-Loop Support

`serena init` and MCP client configuration are human setup steps. Optional JetBrains path requires IDE installation and plugin licensing. Day-to-day coding tasks are driven by the agent once wired.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain ripgrep + sed** | No symbol graph; brittle for multi-file refactors |
| **Generic LSP CLI** | Not packaged as **MCP tools** with agent-oriented workflows and memory |
| **Cloud-only code assistants** | May not give the same **local repo + LSP** control loop for arbitrary OSS stacks |

---

## Use Cases

- **Large-repo navigation** — agent finds symbols and references without reading entire trees into context
- **Safe refactors** — rename/move with IDE-grade semantics instead of text substitution
- **Long sessions** — memory system supports multi-step agent projects
- **Polyglot monorepos** — LSP matrix covers many languages in one MCP server
