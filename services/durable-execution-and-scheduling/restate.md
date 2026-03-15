# Restate

> **"Durable execution for AI agents — any framework, any cloud."**

| | |
|---|---|
| **Website** | https://restate.dev |
| **Docs** | https://docs.restate.dev |
| **GitHub** | https://github.com/restatedev/restate |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |
| **License** | BSL 1.1 (open-source) + Restate Cloud |

---

## Official Website

https://restate.dev

---

## Official Repo

https://github.com/restatedev/restate — Core runtime (open-source)

https://github.com/restatedev/sdk-python — Python SDK

https://github.com/restatedev/sdk-typescript — TypeScript SDK

https://github.com/restatedev/ai-examples — AI agent examples (A2A, MCP, durable agents)

---

## Agent Skills

**Status:** ⚠️ No official skill published by Restate yet.

```bash
npx clawhub@latest search restate durable
```

---

## MCP

**Status:** ✅ MCP examples available

Restate provides examples for building durable MCP servers and A2A (agent-to-agent) communication patterns using its execution runtime.

| Detail | Value |
|---|---|
| **Examples** | https://github.com/restatedev/ai-examples |
| **MCP Integration** | Durable MCP handlers that survive failures |
| **A2A Support** | Reliable agent-to-agent calls with exactly-once semantics |

---

## What It Does

Restate is a durable execution runtime that persists every step of an agent's execution — LLM calls, tool invocations, routing decisions — in a journal. If an agent crashes mid-execution, Restate resumes it from exactly where it left off without re-running completed steps or duplicating side effects.

Unlike Trigger.dev or Inngest (which require using their specific task abstraction), Restate works as lightweight middleware on top of existing agent frameworks (Vercel AI SDK, OpenAI Agents SDK, LangGraph, CrewAI) — developers add durable execution with a few lines of code, without rewriting their agents.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Dedicated docs section: *"AI Agents"* and *"Durable Agents"*; blog: *"Agentic Workflows Are Just Code"*; examples repo dedicated to AI/A2A/MCP patterns |
| **Agent-specific primitive** | Durable AI loop (journal-based); crash-proof HITL with timeouts; A2A reliable communication; compensation patterns for undo on failure; suspend-when-idle cost savings |
| **Autonomy-compatible control plane** | Agents auto-resume from last completed step; rate limit retries handled automatically; no human re-triggers failed runs |
| **M2M integration surface** | Python SDK, TypeScript SDK, REST API; lightweight middleware on existing agent frameworks |
| **Identity / delegation** | Per-invocation IDs; complete observability — pause, resume, restart agents at execution time |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Durable AI Loop** | Every LLM call and tool execution persisted in a journal; crash recovery without re-executing completed steps |
| **Suspend-When-Idle** | Agents suspend when waiting (for HITL, for an event) and resume at zero infrastructure cost |
| **Compensation Pattern** | On failure, automatically undo previous side effects (e.g., cancel a payment if a later step fails) |
| **HITL with Crash-Proof Timeout** | Agent suspends awaiting human input; if timeout expires, compensation runs; no polling |
| **A2A Reliable Communication** | Agent-to-agent calls with exactly-once execution semantics |
| **Complete Observability** | Pause, resume, or restart any running agent from the Restate UI or API |

---

## Autonomy Model

```
Existing agent code wrapped with Restate middleware (2-5 lines)
    ↓
Agent executes — each step recorded in Restate's journal
    ↓
If LLM rate-limited: automatic retry after backoff, no step duplication
    ↓
If agent process crashes: Restate resumes from last journal entry
    ↓
If HITL gate reached: agent suspends (no resource cost); resumes on approval
    ↓
If later step fails: compensation pattern undoes earlier side effects
```

---

## How Restate Differs from Trigger.dev / Inngest

| Dimension | Restate | Trigger.dev / Inngest |
|---|---|---|
| Integration model | Middleware on existing agent code | Requires using their task abstraction |
| Framework support | Any framework (Vercel AI, OpenAI Agents, LangGraph…) | Framework-specific integration |
| Deployment | Self-host or Restate Cloud | Hosted SaaS |
| A2A | Built-in exactly-once A2A | Not a primary primitive |
| Compensation | Native pattern | Not built-in |

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install restate-sdk` |
| TypeScript SDK | `npm install @restatedev/restate-sdk` |
| REST API | Agent management and execution control |
| Vercel AI SDK | Native integration guide |
| OpenAI Agents SDK | Native integration guide |
| Restate Cloud | Managed hosted deployment |
| Self-hosted | Open-source Docker deployment |

---

## Human-in-the-Loop Support

First-class native primitive. Agents call `ctx.run_with_timeout()` or equivalent — execution suspends durably until a human sends an approval event. If timeout expires, compensation runs automatically. No polling, no blocked threads.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Step Functions** | Workflow DSL for human-defined deterministic processes; no LLM-specific journal, no mid-execution pause/resume |
| **Redis queues (BullMQ)** | Job queue; no journal, no compensation, no agent-to-agent exactly-once semantics |
| **No retry logic (bare LangChain)** | No persistence; crash = lost agent state and repeated side effects |

---

## Use Cases

- **Long-horizon research agents** — agent runs for hours; Restate handles all failures and resumes without data loss
- **Financial agents** — compensation pattern undoes a payment initiation if a downstream step fails
- **Multi-agent pipelines** — A2A calls between specialist agents with exactly-once delivery guarantees
- **HITL agents** — agent waits for manager approval; Restate suspends and resumes without resource cost
- **Any existing agent framework** — add durable execution to a LangGraph, CrewAI, or Vercel AI SDK agent with minimal code changes
