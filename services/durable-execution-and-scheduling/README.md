# Durable Execution & Scheduling Services

> Services that let AI agents run **long-horizon, fault-tolerant workflows** with automatic state checkpointing, intelligent retries, and first-class human-in-the-loop pause/resume primitives.

## Why This Category Exists

AI agents have a failure mode that traditional software does not: **compounding probabilistic failures**. A five-step agent workflow where each step succeeds 99% of the time has only 95% overall success probability — and real-world tool calls (API timeouts, LLM rate limits, external service failures) fail far more often than 1%.

Traditional background job systems (SQS, Celery, cron) handle retries for stateless functions. But agents are stateful — if a step fails mid-reasoning-chain, a naive retry starts the whole chain over, losing all intermediate context and wasting expensive LLM calls.

Durable execution for agents requires:

1. **Checkpointing between steps** — each completed step is durably persisted; failures resume from the last checkpoint
2. **Context preservation** — when retrying after failure, the agent's reasoning state is restored, not discarded
3. **Long-running without timeouts** — agent tasks may take hours or days; standard serverless functions (Lambda: 15 min, Vercel: 60 sec) cannot host them
4. **Human-in-the-loop as a first-class primitive** — suspend execution pending human approval, resume when approved
5. **Streaming back to frontends** — users see progress in real time, even for long-running tasks

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Trigger.dev](trigger-dev.md) | Build and deploy fully-managed AI agents and workflows | TypeScript SDK, REST API, Cron | ❌ |
| [Inngest](inngest.md) | Durable execution for AI agents in production | TypeScript SDK, Python SDK, REST API | ✅ |
| [Kitaru](kitaru.md) | Durable execution for AI agents — primitives first, frameworks second | Python SDK, CLI (`--output json`), MCP server | ✅ |
| [Restate](restate.md) | Durable execution for AI agents — any framework, any cloud | Python SDK, TypeScript SDK, REST API | ✅ |
| [MCP-Cloud (mcp-agent)](mcp-cloud-mcp-agent.md) [![⭐](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social)](https://github.com/lastmile-ai/mcp-agent) | Host mcp-agents on cloud — Temporal-backed durable MCP servers | `uvx mcp-agent` CLI, HTTPS MCP endpoint, secrets, observability | ✅ |
| [Inferable](inferable.md) [![⭐](https://img.shields.io/github/stars/inferablehq/inferable?style=social)](https://github.com/inferablehq/inferable) | Reliable AI workflows — humans in the loop, structured outputs, durable execution | TypeScript SDK, Python SDK, REST API, Slack/email HITL | ⚠️ |



## Weekly Impact Update (2026-05-11 → 2026-05-18)

- 详见独立周报文档：[weekly-impact-2026-05-18.md](weekly-impact-2026-05-18.md)

- **Inferable**: 在“durable execution + HITL + structured outputs”方向讨论升温，适合生产级 agent workflow。
- **MCP-Cloud (mcp-agent)**: Temporal-backed durable MCP server 架构持续受到关注，适合长周期任务与失败恢复场景。

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **step-level checkpointing** — failures resume from the last completed step, not from scratch.
2. Support **no-timeout long-running tasks** — agents can run for hours or days.
3. Include a **first-class HITL suspend/resume primitive** — not just a workaround.
4. Preserve **agent reasoning context** across retries and failures.
5. Understand **agent-specific failure modes** — probabilistic outputs, LLM rate limits, tool failures.
