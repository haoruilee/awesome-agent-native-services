# Observability & Tracing Services

> Services that give teams **structured visibility into agent execution** — capturing the full trajectory of an agent's reasoning, tool calls, memory accesses, and outputs in a semantic format that humans can inspect and improve upon.

## Why This Category Exists

Debugging a traditional application means reading logs. Debugging an AI agent means understanding a fundamentally different kind of execution: probabilistic, multi-step, with interleaved LLM calls, tool invocations, context injections, and branching decision paths.

Traditional observability tools (Datadog, CloudWatch, Splunk) were built for:
- Request/response latency and error rates
- Infrastructure metrics (CPU, memory, network)
- Structured log queries

They are not designed to answer agent-specific questions:
- Which tool call caused the agent to take the wrong branch?
- How much of the context window was consumed by memory injection?
- Did the agent reach the right conclusion via a different reasoning path than expected?
- Which prompt version produces better tool selection across 1,000 runs?

Agent-native observability services capture **agent trajectory** — the semantic structure of an agent's execution — and provide evaluation primitives that turn production traces into training datasets.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Langfuse](langfuse.md) | Open-source LLM observability, tracing, and evaluation | OpenTelemetry, Python SDK, TypeScript SDK | ❌ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Capture **agent-specific semantic structure** — tool calls, LLM calls, context injections — not just generic logs.
2. Provide **trajectory replay** — ability to reconstruct and inspect an agent's full execution.
3. Support **dataset-based evaluation** — convert production traces into eval cases.
4. Support **cost and token attribution** per agent run.
5. Integrate with **OpenTelemetry or an agent-specific tracing standard**.
