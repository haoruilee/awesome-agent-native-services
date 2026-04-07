# Runloop

> **"Your AI Agent Accelerator."**

| | |
|---|---|
| **Website** | https://runloop.ai |
| **Docs** | https://docs.runloop.ai |
| **GitHub** | https://github.com/runloopai/api-client-python |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/runloopai/api-client-python?style=social)](https://github.com/runloopai/api-client-python) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **Compliance** | SOC 2 · HIPAA · GDPR (per marketing site) |

---

## Official Website

https://runloop.ai

---

## Official Repo

https://github.com/runloopai/api-client-python — Python API client

https://github.com/runloopai/api-client-ts — TypeScript API client

https://github.com/runloopai/rl-cli — Runloop CLI (`rli`) including MCP server

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + **CLI** + **MCP**

1. Register at [platform.runloop.ai](https://platform.runloop.ai) and create an API key ([settings](https://runloop.ai/settings)).
2. Create isolated **Devboxes** (micro-VM sandboxes) and run commands, snapshots, and blueprints — [Devboxes overview](https://docs.runloop.ai/docs/devboxes/overview).

```bash
pip install runloop-api-client
# or: npm install @runloop/api-client  (see GitHub api-client-ts)
export RUNLOOP_API_KEY=...
```

**CLI + MCP for assistants:**

```bash
npm install -g @runloop/rl-cli
export RUNLOOP_API_KEY=...
rli mcp install   # Claude Desktop config
rli mcp start     # stdio MCP server
```

See [Runloop CLI](https://docs.runloop.ai/docs/tools/rl-cli).

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add …` pack from Runloop yet.

```bash
npx clawhub@latest search runloop
```

---

## MCP

**Status:** ✅ Available (via official CLI)

The Runloop CLI embeds a **Model Context Protocol** server so tools like Claude can list, create, and manage Devboxes — `rli mcp start` (stdio) or `rli mcp start --http` — [Runloop CLI — MCP](https://docs.runloop.ai/docs/tools/rl-cli).

| Detail | Value |
|---|---|
| **Docs** | https://docs.runloop.ai/docs/tools/rl-cli |
| **Install helper** | `rli mcp install` for Claude Desktop |
| **Devbox MCP injection** | Devbox create supports MCP gateway configurations (CLI reference) |

---

## What It Does

Runloop provides **Devboxes**: secure, isolated sandboxes for running **AI-generated code** and long-running agent workflows, with fast startup, optional suspend/resume, **disk snapshots and branching** for agent state, repo-aware environments, secrets/objects stores, and **benchmark jobs** to evaluate coding agents (e.g., SWE-Bench-style runs). The surface area is explicitly marketed for **AI agents** and **AI software engineering** workloads—not generic batch VMs only.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Your AI Agent Accelerator"* and *"Launch AI agents on secure code sandboxes"*; *"Devboxes are code sandbox development environments… for… AI Agents"* — [runloop.ai](https://runloop.ai) |
| **Agent-specific primitive** | **Devbox** lifecycle; **snapshot/branch disk state** for agent trajectories; **benchmark jobs** for agent evaluation; **MCP** wiring from CLI and devbox config |
| **Autonomy-compatible control plane** | API-driven create/exec/suspend/shutdown; no human SSH session required for automation |
| **M2M integration surface** | Python/TS API clients, REST, CLI, MCP via `rli` |
| **Identity / delegation** | Per-devbox IDs; API keys; secrets injection; audit-friendly logging (per product docs) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Devbox** | Isolated execution environment for agent code (micro-VM + container isolation, per product) |
| **Snapshot** | Capture and branch disk state for reproducible agent runs |
| **Blueprint** | Reusable image/template for agent environments |
| **Benchmark job** | Orchestrated multi-agent evaluation against public or custom scenarios |
| **Object / secret store** | Agent artifacts and credentials without embedding secrets in prompts |
| **Suspend / resume** | Cost-aware pausing of bursty agent workflows |

---

## Autonomy Model

```
Agent obtains RUNLOOP_API_KEY (or delegated token)
    ↓
Creates Devbox from blueprint or snapshot via API/CLI
    ↓
Runs commands, tests, or full agent loop inside sandbox
    ↓
Snapshots state for regression tests or parallel branches
    ↓
Shuts down, suspends, or resumes without human provisioning
```

---

## Identity and Delegation Model

- **API keys** — tenant-scoped access to Runloop API
- **Devbox IDs** — isolate sessions and attribute logs
- **Secrets** — injected as env vars without surfacing values to the LLM (pattern documented in CLI)
- **Network policies** — optional egress and MCP gateway controls (CLI reference)

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install runloop-api-client` — [api-client-python](https://github.com/runloopai/api-client-python) |
| TypeScript SDK | `@runloop/api-client` — [api-client-ts](https://github.com/runloopai/api-client-ts) |
| REST API | Platform API per [docs.runloop.ai](https://docs.runloop.ai) |
| CLI | `npm install -g @runloop/rl-cli` → `rli` |
| MCP | `rli mcp start` / `rli mcp install` |

---

## Human-in-the-Loop Support

Optional review of agent outputs or benchmark results. Core sandbox execution does not require a human in the loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw cloud VMs** | No agent-first lifecycle, snapshot branching for trajectories, or built-in agent benchmark orchestration |
| **CI runners** | Job-centric; not optimized for interactive agent loops, suspend/resume, or MCP-native assistant control |
| **Local Docker** | Host risk and ops burden; lacks managed agent evaluation and fleet scale patterns |

---

## Use Cases

- **Coding agents** — run, test, and iterate generated code in isolated Devboxes
- **Agent CI / regression** — snapshot state and re-run after model or prompt changes
- **Benchmarking** — compare agent implementations on public suites at scale
- **Long-horizon tasks** — suspend/resume bursty workloads to control cost
