# Inferable

> **"Build reliable AI Workflows and Agents with humans in the loop, structured outputs and durable execution."**

| | |
|---|---|
| **Website** | https://inferable.ai |
| **Docs** | https://docs.inferable.ai |
| **GitHub** | https://github.com/inferablehq/inferable |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling](README.md) |
| **Stars** | 437+ |

---

## Official Website

https://inferable.ai

---

## Official Repo

https://github.com/inferablehq/inferable

---

## How to Use (Agent Onboarding)

```
# Self-hosted (Docker Compose) or hosted SaaS — pick one.
# SDK install:
npm install @inferable/sdk
# or
pip install inferable

# Then wrap a function as a durable workflow step:
from inferable import workflow

@workflow.step()
def call_tool(...): ...
```

HITL gates are added with one decorator; suspends the workflow durably while waiting for a human.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

Search:

```bash
npx clawhub@latest search inferable
```

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server. The SDK and REST API are the primary surfaces for now; community MCP wrappers exist.

| Detail | Value |
|---|---|
| **MCP Repo** | (community) |
| **Transport** | n/a — primary surface is SDK + REST |
| **Compatible Clients** | any agent runtime that calls REST or imports the SDK |

---

## What It Does

Inferable is a managed durable-execution runtime built specifically for AI workflows and agents. It provides three tightly integrated primitives that, taken together, distinguish it from generic workflow engines:

1. **Durable execution** — every step is checkpointed; agent crashes resume from the last successful step instead of re-running expensive LLM calls.
2. **First-class HITL** — `await human_approval(...)` suspends the workflow without blocking a process; humans approve via Slack or email; the workflow resumes when they reply.
3. **Structured outputs + versioned workflows** — outputs are schema-validated; workflows are versioned so deployments don't break in-flight runs.

It overlaps in spirit with Trigger.dev / Inngest / Restate (already in this catalog) but takes a more opinionated agent-shaped stance: HITL approval is built in (not a pattern), structured outputs are first-class, and the SDK assumes LLM/tool calls are the work.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline: *"Build reliable AI Workflows and Agents with humans in the loop, structured outputs and durable execution"* |
| **Agent-specific primitive** | Built-in async human approval gate, schema-validated structured outputs, agent crash recovery |
| **Autonomy-compatible control plane** | Agent runs the workflow; HITL is opt-in per step; workflows survive process crashes |
| **M2M integration surface** | TS / Python SDK + REST API + Slack/email HITL channels |
| **Identity / delegation** | Workflow runs are versioned and attributable; HITL approvals are signed by approver identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Durable Step** | Checkpointed unit of work; resumes after crash without re-execution |
| **Human Approval Gate** | `await human_approval(...)` — durable suspend until Slack/email reply |
| **Structured Output** | Schema-validated step output; type-safe in SDK |
| **Versioned Workflow** | Deploy a new version without breaking in-flight runs |
| **Backward-Compatible Replay** | Old runs continue to use their original workflow version |

---

## Autonomy Model

1. Developer defines a workflow in code (`@workflow.step()`-decorated functions).
2. Agent triggers the workflow via SDK or REST.
3. Each step's output is checkpointed; if the process dies, the workflow resumes from the last good checkpoint.
4. When a step calls `human_approval(...)`, the workflow suspends durably; a Slack/email message goes to the configured approver.
5. Approver replies; workflow resumes.

The agent never blocks a thread waiting for a human, and never re-executes expensive LLM calls after a crash.

---

## Identity and Delegation Model

- Each run has a stable run ID.
- HITL approvals carry the approver's identity in the audit trail.
- Workflow versions are immutable; rolling out a new version creates a new version slot, not an in-place edit.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `@inferable/sdk` |
| Python SDK | `inferable` |
| REST API | Trigger / inspect / cancel runs |
| Slack / email channels | HITL approval surfaces |

---

## Human-in-the-Loop Support

HITL is the centerpiece. `human_approval(...)` durably suspends the run; reminder + escalation + timeout policies are first-class. Compared to HumanLayer (Python decorator pattern), Inferable's HITL is integrated with the durable workflow engine — i.e. the suspended run survives a process restart.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Trigger.dev / Inngest / Restate** | Excellent durable engines, but HITL is a pattern you build, not a primitive; structured outputs aren't first-class |
| **Temporal** | Generic durable execution; not LLM/agent-shaped; no out-of-the-box Slack/email HITL |
| **Plain Lambda + DynamoDB checkpoint** | No replay, no version semantics, no HITL primitive |

---

## Use Cases

- **High-stakes agent actions** — agent must wait for an approver to confirm a refund / wire / firing-the-customer email
- **Long-horizon research** — multi-day workflows that survive sandbox restarts
- **Multi-step structured pipelines** — each step's output schema is validated, so downstream agents don't see malformed data
- **Versioned production rollouts** — deploy a new agent workflow version without breaking yesterday's in-flight runs
