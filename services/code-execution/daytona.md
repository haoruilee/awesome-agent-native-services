# Daytona

> **"Run AI Code. Secure and Elastic Infrastructure for Running Your AI-Generated Code."**

| | |
|---|---|
| **Website** | https://daytona.io |
| **Docs** | https://www.daytona.io/docs |
| **GitHub** | https://github.com/daytonaio/daytona |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/daytonaio/daytona?style=social)](https://github.com/daytonaio/daytona) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | AGPL-3.0 |

---

## Official Website

https://daytona.io

---

## Official Repo

https://github.com/daytonaio/daytona — Core platform (open source)

SDKs documented in README: Python (`pip install daytona`), TypeScript (`@daytonaio/sdk`), Ruby, Go

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + `REST` + `MCP (via Daytona CLI)`

```bash
pip install daytona
# or: npm install @daytonaio/sdk
```

Create and use **Sandboxes** via SDK — see [Sandboxes](https://www.daytona.io/docs/en/sandboxes/) for lifecycle, filesystem, Git, process execution, and LSP.

**MCP for Claude, Cursor, Windsurf:**

```bash
brew install daytonaio/cli/daytona   # or Windows installer from docs
daytona login
daytona mcp init cursor   # or claude / windsurf
# Manual: daytona mcp config  →  paste JSON into agent MCP settings
daytona mcp start
```

Full guide: [Daytona MCP](https://www.daytona.io/docs/en/mcp/).

---

## Agent Skills

**Status:** ⚠️ No dedicated `npx skills add daytonaio/skills` entry in catalog yet — onboarding is docs + MCP + SDK.

```bash
npx clawhub@latest search daytona sandbox
```

---

## MCP

**Status:** ✅ Available (ships with Daytona CLI)

| Detail | Value |
|---|---|
| **Docs** | https://www.daytona.io/docs/en/mcp/ |
| **Start** | `daytona mcp start` (after `daytona login`) |
| **Init helpers** | `daytona mcp init claude|cursor|windsurf` |
| **Config export** | `daytona mcp config` |
| **Tool areas** | Sandbox management, filesystem, Git, process/code execution, computer use, preview (per official docs) |
| **Compatible Clients** | Claude, Cursor, Windsurf, others via pasted JSON config |

---

## What It Does

Daytona provides **isolated Sandboxes** — ephemeral, API-controlled compute environments optimized for **running AI-generated code** safely away from the developer's laptop. Agents create sandboxes in milliseconds, execute commands with streaming output, manipulate files, run Git operations, use **LSP** for editor-grade language services, and can expose **preview URLs** for web apps running inside the sandbox. The **Daytona MCP server** exposes these capabilities as tools so coding agents in Claude, Cursor, or Windsurf can provision and drive sandboxes without custom glue code.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub repo description: *"Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code"*; README tagline: *"Run AI Code"* — [source](https://github.com/daytonaio/daytona) |
| **Agent-specific primitive** | **Programmatic Sandbox** as the unit of execution — sub-second creation, isolated kernel/filesystem/network, **forkable state** (roadmap), **OCI images** — designed for machine-generated workloads, not human SSH sessions |
| **Autonomy-compatible control plane** | Agents create/destroy sandboxes and run code via SDK/API; MCP tools map directly to sandbox ops without per-command human approval |
| **M2M integration surface** | Python, TypeScript, Ruby, Go SDKs; REST; **Daytona CLI** with **`daytona mcp start`** |
| **Identity / delegation** | **Per-sandbox isolation**; **`daytona login`** / API credentials scope what the agent can provision; audit via platform logs and sandbox lifecycle |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox** | Isolated environment with CPU/RAM/disk quotas; primary execution unit |
| **Fast create** | Sub-90ms sandbox creation (per README marketing) |
| **Process execution** | Run agent-generated commands with streaming I/O |
| **Filesystem API** | CRUD and permissions inside the sandbox |
| **Git operations** | Clone and manipulate repos inside the sandbox |
| **LSP** | Language-server integration for multi-language agent coding |
| **Preview** | URLs to inspect running web apps from the agent loop |
| **MCP tools** | Sandbox + FS + Git + exec + computer use + preview (per MCP docs) |

---

## Autonomy Model

```
Agent (or orchestrator) authenticates: daytona login / API token
    ↓
Agent creates Sandbox via SDK or MCP tool
    ↓
Agent runs installs, tests, servers — streams output back to the model
    ↓
Agent snapshots or destroys sandbox when task completes
```

---

## Identity and Delegation Model

- **Sandbox ID** — Each run is attributable to a sandbox instance; logs tie actions to that unit.
- **Org / user credentials** — `daytona login` binds MCP and CLI to a Daytona account; rotate tokens if an agent is compromised.
- **Network egress** — Operators configure what outbound access sandboxes may use (per deployment policy).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install daytona` |
| TypeScript SDK | `npm install @daytonaio/sdk` |
| Go / Ruby | See repo README |
| REST / platform API | https://www.daytona.io/docs |
| CLI + MCP | `daytona mcp start` |

---

## Human-in-the-Loop Support

Humans use the dashboard and logs for debugging; the agent path is API/MCP-first. Long-running sandboxes may require org policy for cost and data retention — not a product-level approval gate on each exec call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Docker on developer machine** | No **agent-scoped** sub-90ms API, no first-class **MCP** tool surface, no unified Git/LSP/preview story for coding agents |
| **Generic CI runners** | Job-centric, not **sandbox-per-agent-turn** with LSP and preview for interactive codegen loops |

---

## Use Cases

- **Coding agents** — Run generated code, tests, and dev servers in isolation with preview links
- **Data / analysis agents** — Spin up Python or Node sandboxes for notebook-style execution without host risk
- **Multi-step codegen** — Durable sandbox state across many model turns before teardown
