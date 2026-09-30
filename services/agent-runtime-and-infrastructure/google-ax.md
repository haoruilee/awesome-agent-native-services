# Agent Executor (AX)

> **"An open source distributed agent runtime"**

| | |
|---|---|
| **Website** | https://agentexecutor.io |
| **Docs** | https://github.com/google/ax#readme |
| **GitHub** | https://github.com/google/ax |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/google/ax?style=social)](https://github.com/google/ax) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) released 2026-09-25; last GitHub push 2026-09-27; 12,569 stars; Apache-2.0; README still warns AX is in heavy development; [agentexecutor.io](https://agentexecutor.io) HTTP 200 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://agentexecutor.io

---

## Official Repo

https://github.com/google/ax

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + optional gRPC server

```bash
go install github.com/google/ax/cmd/ax@latest
ax --help

# Local built-in Antigravity harness (needs GEMINI_API_KEY or Vertex ADC)
ax --input "Can you list this directory?"

# Resume
ax --conversation <id> --input "Show me the contents of README.md"
ax --conversation <id> --resume
```

Remote controller:

```bash
ax serve --config ax.yaml
ax --input "Hello agents!" --server localhost:8494
```

Kubernetes on [Agent Substrate](agent-substrate.md) (`https://github.com/agent-substrate/substrate`) is the documented production-oriented deploy path (`manifests/README.md`). AX is the harness runtime; Substrate is the separate K8s compute control plane.

---

## Agent Skills

**Status:** ⚠️ Hosted by the harness, not a published `npx skills add` package

Built-in harnesses such as Antigravity can load Agent Skills when configured. A `Workspace` manifest can pre-wire skill packages from a registry into `/.agents/skills` ([docs/manifests.md](https://github.com/google/ax/blob/main/docs/manifests.md)). There is no official `npx skills add google/ax` command.

Search community skills: `npx clawhub@latest search agent-executor`. See: https://agentskills.io/specification

---

## MCP

**Status:** ⚠️ Consumer, not a published MCP server

Antigravity can discover and call MCP tools when they are configured. AX does not ship a standalone MCP server package for controlling the runtime.

---

## What It Does

AX (Agent Executor) is a self-hosted distributed harness runtime from Google. It provisions isolated environments from suspendable/resumable images, runs harnesses and agents, and keeps durable execution state in an event log so work can resume after failure. It is compute-agnostic, with the best-documented path on Kubernetes via Agent Substrate. Official text says AX is **not** a managed service and **not** an agentic framework.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub: **"An open source distributed agent runtime"**. README: **"AX, short for Agent Executor, is a distributed harness runtime."** — [google/ax](https://github.com/google/ax) |
| **Agent-specific primitive** | Conversation-scoped isolated harness execution with an event log, single-writer controller, and resume/suspend — not a generic job queue |
| **Autonomy-compatible control plane** | `ax --input` / `--resume` continues work without a human clicking a UI. Human approval is a roadmap item (elicitation), not a per-step requirement today |
| **M2M integration surface** | `ax` CLI, `ax serve` gRPC, YAML config, Kubernetes manifests |
| **Identity / delegation** | Conversation IDs, optional `--agent` IDs, per-request `--agent-config`. Session-tenant actors on the control service. No user-OAuth delegation product |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Conversation** | Durable execution id you can continue or resume |
| **Event log** | SQLite (default example) scan/append store for recovery |
| **Harness isolation** | Harnesses/skills/tools/agents as isolated actors |
| **Resumption** | Recover incomplete executions; compute-layer suspend on compatible platforms |
| **Built-in Antigravity harness** | Default local harness; Gemini API or Vertex |

---

## Autonomy Model

```
Operator installs ax CLI and sets model credentials
    -> ax --input starts a conversation (UUID if omitted)
    -> controller appends the event log and runs the harness actor
    -> later: ax --conversation <id> --input … or --resume
    -> optional ax serve for a remote gRPC controller
```

README warns of breaking changes before a stable release. External PRs are paused.

---

## Identity and Delegation Model

- **Conversation ID:** The handle for resume and follow-up input.
- **Agent ID / config:** Optional `--agent`, `--agent-config`, or `--agent-config-file`.
- **Single-writer controller:** Consistent state; not a multi-leader cluster story in the README.
- **Not a managed identity service:** You run AX; model keys are yours (`GEMINI_API_KEY` or Vertex ADC).
- **Agent Substrate:** Isolation/resume substrate is optional and listed separately; not added here.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `ax`, `ax serve`, `--conversation`, `--resume`, `--server` |
| gRPC | Controller when `--server` is set (default example `:8494`) |
| Config | `ax.yaml` (`version: v1alpha`) |
| K8s | `manifests/` + Agent Substrate |

---

## Human-in-the-Loop Support

Not a productized approval plane. Roadmap lists elicitation. Operators resume conversations from the CLI. Long idle periods are why AX wants suspend/resume rather than a human babysitting the actor.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Kubernetes Job / Deployment** | Designed for stateless services or batch, not suspendable sandboxed agent actors with an event log |
| **Agent framework (LangGraph, etc.)** | AX explicitly is not a framework; frameworks can run *as* harnesses |
| **Hosted agent builder** | AX is self-hosted runtime infrastructure |

---

## Use Cases

- **Long-running agent work** — resume after interruption with a conversation id
- **Isolated harnesses** — run tools/skills/agents as separate actors
- **K8s agent density** — documented path via Agent Substrate (not catalogued here)
- **Local experiments** — `ax --input` with the built-in harness
