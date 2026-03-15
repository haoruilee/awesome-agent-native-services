# Inngest

> **"Durable execution for AI agents in production."**

| | |
|---|---|
| **Website** | https://inngest.com |
| **Docs** | https://www.inngest.com/docs |
| **GitHub** | https://github.com/inngest/inngest |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |

---

## What It Does

Inngest provides a durable execution platform specifically addressing the production challenges of AI agents. It checkpoints state between tool calls, handles external API failures through intelligent retries that preserve agent context, and maps human-in-the-loop approval patterns to native suspend/resume primitives. In 2025, durable execution became a mainstream requirement as AWS, Cloudflare, and Vercel all launched competing offerings — Inngest was ahead of this trend.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | 2025 blog: *"Durable Execution: The Key to Harnessing AI Agents in Production"*; agent failure modes (probabilistic behavior, compositionality, statefulness) are the design brief |
| **Agent-specific primitive** | Checkpoint between tool calls (not just between functions); HITL suspend/resume; context-preserving retry; low-latency patterns for interactive agents |
| **Autonomy-compatible control plane** | Agents resume automatically from last checkpoint; no human re-triggers failed runs |
| **M2M integration surface** | TypeScript SDK, Python SDK, REST API |
| **Identity / delegation** | Per-run event IDs; full execution history attributable to specific agent runs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Durable Step** | Each `step.run()` is checkpointed; failures retry only the failed step |
| **Context-Preserving Retry** | On retry, agent reasoning context from previous steps is restored |
| **HITL Suspend/Resume** | `step.waitForEvent()` or `step.sleep()` patterns for approval gates |
| **Low-Latency Pattern** | Optimized for interactive, real-time agent responses (not just async batch) |
| **Checkpoint Between Tool Calls** | State persisted after each tool call — agent doesn't restart the whole chain on failure |
| **Event-Driven Triggers** | Agents triggered by external events, webhooks, or cron |

---

## Why This Matters for Agents: The Compounding Failure Problem

```
5-step agent workflow:
  Step 1: 99% success
  Step 2: 99% success
  Step 3: 99% success
  Step 4: 99% success
  Step 5: 99% success

Without durable execution: 0.99^5 = 95% overall success
With durable execution: 99% success per step, independently

At scale (10,000 agent runs/day):
  Without durable execution: 500 failed runs/day
  With durable execution: ~50 failed runs/day, all auto-recovered
```

---

## Autonomy Model

```
Agent function defined with Inngest step() primitives
    ↓
Triggered by event, webhook, or cron
    ↓
Each step.run() is checkpointed on completion
    ↓
If LLM rate limit or API failure: automatic retry after backoff
    ↓
Reasoning context from previous steps is preserved on retry
    ↓
HITL gate: step.waitForEvent() suspends until approval event received
    ↓
Resumes automatically when approval event arrives
```

---

## Identity and Delegation Model

- Per-run event IDs enable attribution and debugging
- HITL events include approval metadata (who approved, when, context provided)
- Event history is queryable for audit and debugging

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `inngest.createFunction()`, `step.run()`, `step.sleep()`, `step.waitForEvent()` |
| Python SDK | Equivalent Python API |
| REST API | Event triggering, function management |
| Webhooks | External event triggers |
| Cron | Native cron schedule support |

---

## Human-in-the-Loop Support

Native through `step.waitForEvent()` — agent suspends execution durably (not blocking a thread) until an approval event arrives. The event can be sent by a human via any channel (Slack bot, email link, dashboard button). Agent resumes automatically.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS SQS** | Message queue; no step-level checkpointing, no context preservation on retry |
| **AWS Step Functions** | Workflow orchestration for human-defined deterministic processes; designed for predictable, stateless steps |
| **Redis Queues (BullMQ)** | Job queue; no agent context preservation, no HITL primitive |
| **Celery** | Python task queue; no step-level state, no agent-specific retry semantics |

---

## Use Cases

- **Interactive agents** — real-time agents that must respond quickly while durably tracking multi-step workflows
- **Tool-heavy agents** — agents making many external API calls where any call might fail
- **Multi-day research** — agents that run long research tasks spanning multiple LLM sessions
- **Financial agents** — agents with approval gates before executing irreversible financial actions
- **Monitoring agents** — event-driven agents triggered by external conditions requiring durable, multi-step responses
