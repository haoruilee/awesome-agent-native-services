# Kitaru

> **"Durable execution for AI agents — primitives first, frameworks second."**

| | |
|---|---|
| **Website** | https://kitaru.ai |
| **Docs** | https://kitaru.ai/docs |
| **GitHub** | https://github.com/zenml-io/kitaru |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/zenml-io/kitaru?style=social)](https://github.com/zenml-io/kitaru) |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |
| **License** | Apache 2.0 (open-source) |

---

## Official Website

https://kitaru.ai

---

## Official Repo

https://github.com/zenml-io/kitaru — Python SDK, CLI, MCP server, and framework adapters

---

## Agent Skills

**Status:** ⚠️ No official skill published yet.

```bash
npx clawhub@latest search kitaru durable
```

For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available (optional `kitaru[mcp]` extra)

Kitaru ships an MCP server that exposes execution management, memory operations, stack lifecycle, secrets, and model registry as MCP tools. Agents can start flows, inspect checkpoints, read/write memory, browse artifacts, and replay executions — all through MCP without writing Python.

| Detail | Value |
|---|---|
| **Install** | `pip install kitaru[mcp]` |
| **Transport** | stdio |
| **MCP Tools** | `run_flow`, `get_execution`, `list_executions`, `get_execution_logs`, `replay_execution`, `retry_execution`, `resume_execution`, `cancel_execution`, `memory_store`, `memory_search`, `memory_compact`, `list_stacks`, `create_stack`, `set_secret`, `list_secrets`, and more |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Kitaru is a durable execution layer for AI agents built on top of ZenML. It provides a small set of Python primitives — `@flow`, `@checkpoint`, `save`, `load`, `memory`, `wait`, `log`, `llm` — that make agent workflows persistent, replayable, and observable without requiring a graph DSL or changing Python control flow.

Agents write normal Python functions decorated with `@flow` and `@checkpoint`. Every checkpoint output is automatically persisted. If a flow fails mid-execution, replay resumes from the last completed checkpoint. `kitaru.wait()` suspends execution for human-in-the-loop approval. `kitaru.memory` provides persistent, queryable memory across sessions. `kitaru.llm()` auto-tracks LLM calls with cost and token metadata.

The CLI (`kitaru`) and MCP server provide a full agent-facing control plane: start executions, inspect logs, replay from any checkpoint with artifact overrides, manage secrets, and browse artifacts — all with structured JSON output designed for machine consumption.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Tagline: *"Durable execution layer for AI agents"*; docs, CLI, and MCP server all designed for agent consumption; CLI outputs structured JSON (`--output json`) for machine parsing |
| **Agent-specific primitive** | `@flow` / `@checkpoint` decorators; `kitaru.wait()` for HITL suspend; `kitaru.memory` for persistent agent memory; `kitaru.llm()` for tracked LLM calls; `kitaru.save()` / `kitaru.load()` for artifact persistence; framework adapters (PydanticAI) |
| **Autonomy-compatible control plane** | Checkpoints auto-persist; replay from any point without human intervention; `KitaruClient` for programmatic execution management; MCP server for agent self-service |
| **M2M integration surface** | Python SDK, CLI with `--output json` contract, MCP server (stdio), `KitaruClient` programmatic API |
| **Identity / delegation** | Per-execution IDs; checkpoint-level audit trail; secrets management (`kitaru secrets`); model registry with alias-linked secrets; execution logs with structured metadata |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`@flow`** | Top-level orchestration boundary — defines a durable agent workflow |
| **`@checkpoint`** | Persisted execution step — output cached for replay; the unit of durability |
| **`kitaru.wait()`** | Suspends execution until an external event (human approval, webhook, timeout) |
| **`kitaru.llm()`** | Tracked LLM call with automatic cost, token, and latency metadata |
| **`kitaru.memory`** | Persistent, queryable agent memory across sessions with scoped namespaces |
| **`kitaru.save()` / `kitaru.load()`** | Explicit artifact persistence within checkpoints |
| **`kitaru.log()`** | Structured metadata logging on executions and checkpoints |
| **Replay with overrides** | Re-run a flow from a specific checkpoint, optionally swapping cached outputs |
| **Framework adapters** | `kitaru.adapters.pydantic_ai.wrap(agent)` tracks model requests and tool calls under the enclosing checkpoint |

---

## Autonomy Model

```
Agent defines workflow with @flow and @checkpoint decorators
    ↓
Execution started via flow.run(), CLI, MCP, or KitaruClient
    ↓
Each @checkpoint output is automatically persisted
    ↓
If LLM rate-limited or tool fails: checkpoint-level retry
    ↓
If agent process crashes: replay resumes from last completed checkpoint
    ↓
If HITL gate reached: kitaru.wait() suspends until external event
    ↓
If later step fails: replay from any checkpoint with optional artifact overrides
    ↓
Agent inspects results via KitaruClient, CLI (--output json), or MCP
```

---

## Identity and Delegation Model

- Each execution receives a unique ID; checkpoints within an execution are individually addressable
- `kitaru.log()` attaches structured metadata to executions and checkpoints, providing an audit trail
- Secrets management (`kitaru secrets set/show/list/delete`) scopes credentials per project
- Model registry with alias-linked secrets — `kitaru.llm()` auto-resolves credentials without exposing them to agent code
- `KitaruClient` provides programmatic access to execution history, logs, artifacts, and replay — suitable for agent-to-agent delegation

---

## How Kitaru Differs from Trigger.dev / Inngest / Restate

| Dimension | Kitaru | Trigger.dev / Inngest | Restate |
|---|---|---|---|
| Integration model | Python-native `@flow` / `@checkpoint` decorators | Their task/step abstraction | Middleware on existing frameworks |
| Agent interface | SDK + CLI (`--output json`) + MCP server | SDK + (Inngest) MCP | SDK |
| Built-in memory | `kitaru.memory` — persistent, queryable, with compaction | Not built-in | Not built-in |
| LLM tracking | `kitaru.llm()` auto-tracks cost, tokens, latency | Not built-in | Not built-in |
| Replay | From any checkpoint with artifact overrides | Step-level retry | Journal-based resume |
| Framework adapters | PydanticAI (more planned) | Framework-specific | Any framework via middleware |
| Language | Python-first | TypeScript (Trigger) / TS+Python (Inngest) | Python + TypeScript |
| Deployment | Local zero-config; one-line connect for production (K8s, Vertex, SageMaker, AzureML) | Hosted SaaS | Self-host or Restate Cloud |

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `@flow`, `@checkpoint`, `kitaru.wait()`, `kitaru.llm()`, `kitaru.memory`, `kitaru.save()`, `kitaru.load()`, `kitaru.log()` |
| CLI | `kitaru executions get/list/logs/replay/retry/resume/cancel`, `kitaru secrets`, `kitaru memory`, `kitaru model` — all with `--output json` |
| MCP Server | `pip install kitaru[mcp]` — full execution, memory, stack, and secrets management |
| KitaruClient | Programmatic Python API: `client.executions.get()`, `.list()`, `.logs()`, `.replay()`, `.retry()`, `.resume()`, `.cancel()` |
| Stack backends | Local, Kubernetes, Vertex AI, SageMaker, AzureML |

---

## Human-in-the-Loop Support

First-class native primitive. `kitaru.wait()` suspends a flow durably — execution state is checkpointed and the process can exit. When the external event arrives (human approval, webhook, timeout), the flow resumes from exactly where it left off. PydanticAI adapter supports HITL marker tools via `kitaru.adapters.pydantic_ai.hitl_tool(...)`.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Step Functions** | Workflow DSL for deterministic processes; no LLM-specific primitives, no agent memory, no MCP |
| **Celery / Redis queues** | Job queues; no checkpoint-level persistence, no agent memory, no replay with overrides |
| **Bare LangChain / CrewAI** | No durable persistence; crash = lost agent state; no checkpoint replay |
| **MLflow / W&B** | Experiment tracking for ML training, not durable execution for agent workflows |

---

## Use Cases

- **Long-horizon research agents** — multi-step workflows that run for hours; checkpoints ensure no work is lost on failure
- **HITL approval workflows** — agent suspends at `kitaru.wait()` for human review; resumes automatically when approved
- **Multi-model agent pipelines** — `kitaru.llm()` tracks costs across providers; replay lets you swap models at specific checkpoints
- **Persistent-memory agents** — `kitaru.memory` maintains context across sessions; compaction keeps memory within token budgets
- **Production agent deployments** — zero-config locally, then deploy to Kubernetes, Vertex AI, SageMaker, or AzureML with a stack change
