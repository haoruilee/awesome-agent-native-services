# Trigger.dev

> **"Build and deploy fully-managed AI agents and workflows."**

| | |
|---|---|
| **Website** | https://trigger.dev |
| **Docs** | https://trigger.dev/docs |
| **GitHub** | https://github.com/triggerdotdev/trigger.dev |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |

---

## Official Website

https://trigger.dev

---

## Official Repo

https://github.com/triggerdotdev/trigger.dev

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official skills published at [`triggerdotdev/skills`](https://github.com/triggerdotdev/skills) — see [trigger.dev/docs/skills](https://trigger.dev/docs/skills)

```bash
npx skills add triggerdotdev/skills
```

Install specific skills:

```bash
npx skills add triggerdotdev/skills --skill trigger-tasks
npx skills add triggerdotdev/skills --skill trigger-agents
```

| Skill | What It Teaches the Agent |
|---|---|
| `trigger-setup` | Initialize a Trigger.dev project with correct configuration |
| `trigger-tasks` | Write and deploy background tasks and durable workflows |
| `trigger-agents` | Build LLM workflows and multi-step AI agents with checkpointing |
| `trigger-realtime` | Implement live progress updates and streaming to frontends |
| `trigger-config` | Configure Trigger.dev build and runtime settings |

**Compatibility:** Claude Code, Cursor, Codex, and all [AgentSkills](https://agentskills.io/)-compatible tools.

---

## MCP

**Status:** ⚠️ No dedicated MCP server published

Trigger.dev does not currently provide a standalone MCP server. Tasks are triggered via REST API or cron. The TypeScript SDK integrates with any agentic framework including those that use MCP for tool orchestration.

| Detail | Value |
|---|---|
| **API Docs** | https://trigger.dev/docs |
| **GitHub** | https://github.com/triggerdotdev/trigger.dev |
| **SDK** | TypeScript (primary), with streaming REST API |

---

## What It Does

Trigger.dev provides a durable execution runtime for AI agent tasks with **no timeouts**, type-safe TypeScript agent definitions, first-class human-in-the-loop pause/resume, full observability, and streaming responses to frontends. Agents can run multi-step workflows for hours or days — surviving infrastructure failures through automatic state checkpointing between steps.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | AI agents are the primary product use case; the 2025 product page dedicates a section to AI agent patterns |
| **Agent-specific primitive** | No-timeout long-running tasks; type-safe agent definitions with Zod; HITL pause/resume; streaming frontend response |
| **Autonomy-compatible control plane** | Agents run without timeout limits; checkpointing handles partial failures automatically |
| **M2M integration surface** | TypeScript SDK, REST API, cron scheduling |
| **Identity / delegation** | Per-run task IDs; full execution trace; streaming response attribution |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **No-Timeout Task** | Tasks run for minutes, hours, or days without artificial timeout limits |
| **Step Checkpointing** | Each completed step is persisted; failures resume from last checkpoint |
| **HITL Suspend/Resume** | `waitForApproval()` — agent suspends; resumes automatically when human approves |
| **Type-Safe Agent** | TypeScript + Zod schema definitions with compile-time type safety |
| **Streaming Response** | Real-time token streaming back to frontend during long-running tasks |
| **Observability** | Full execution trace, step timings, error capture |
| **Cron Scheduling** | `@cron("0 9 * * MON")` for scheduled autonomous agent runs |

---

## Autonomy Model

```
Agent task defined as TypeScript code with step() primitives
    ↓
Task triggered via API or cron
    ↓
Each step() is checkpointed on completion
    ↓
If infrastructure failure: resume from last checkpoint
    ↓
If HITL gate: waitForApproval() suspends task
    ↓
Human approves via email/Slack: task automatically resumes
    ↓
Final result returned via streaming response
```

---

## HITL Pattern

```typescript
export const task = trigger.task({
  id: "process-payment",
  run: async (payload) => {
    // Autonomous steps
    const analysis = await step.run("analyze", () => analyzeTransaction(payload));

    // HITL gate for high-risk action
    await step.waitForApproval({
      message: `Approve payment of $${analysis.amount} to ${analysis.recipient}?`,
      timeout: "24h",
    });

    // Resume after approval
    const result = await step.run("execute", () => executePayment(analysis));
    return result;
  },
});
```

---

## Identity and Delegation Model

- Per-run task IDs enable attribution in logs and observability
- HITL approval records who approved, when, and what context was shown
- Cron-triggered runs have their own trace separate from manually triggered runs

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TypeScript SDK | Primary interface — type-safe task definitions, step primitives |
| REST API | Task triggering, status polling, result retrieval |
| Cron | Native `@cron()` decorator for scheduled execution |
| Streaming | Server-sent events for real-time frontend updates |

---

## Human-in-the-Loop Support

First-class native primitive. `step.waitForApproval()` is designed specifically for agent workflows. Approval requests are routed to operators via configurable channels; the task is durably suspended (not blocked) and resumes automatically on approval.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Lambda** | 15-minute timeout; no step checkpointing; no HITL; agent context lost on failure |
| **Vercel Functions** | 60-second timeout; no durable state; not designed for long-running agent tasks |
| **Celery** | Background task queue for Python; no checkpointing between steps, no HITL primitive |
| **cron (raw)** | Scheduling only; no step state, no HITL, no type safety, no streaming |

---

## Use Cases

- **Research agents** — multi-hour research tasks with intermediate checkpoints and human review gates
- **Content generation pipelines** — long-form content generation with approval at key milestones
- **Financial processing agents** — multi-step financial workflows with HITL gates for high-value transactions
- **Data pipeline agents** — ETL agents that run for hours without timeout risk
- **Scheduled monitoring** — agents that run daily/weekly to check conditions and report findings
