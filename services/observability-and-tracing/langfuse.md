# Langfuse

> **"Open-source LLM observability, tracing, and evaluation for AI agents."**

| | |
|---|---|
| **Website** | https://langfuse.com |
| **Docs** | https://langfuse.com/docs |
| **GitHub** | https://github.com/langfuse/langfuse |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Open-source (MIT / enterprise) |

---

## Official Website

https://langfuse.com

---

## Official Repo

https://github.com/langfuse/langfuse — Core platform (open-source)

https://github.com/langfuse/mcp-server-langfuse — Official MCP server

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official skill published at [`langfuse/skills`](https://github.com/langfuse/skills) — listed on [skills.sh/langfuse/skills](https://skills.sh/langfuse/skills)

```bash
npx skills add https://github.com/langfuse/skills --skill langfuse-observability
```

| Skill | What It Teaches the Agent |
|---|---|
| `langfuse-observability` | Instrument LLM applications with Langfuse tracing following best practices: model name, token usage, proper span hierarchy, and framework integrations (OpenAI SDK, LangChain, LlamaIndex, Vercel AI SDK) |

Additional skills from Langfuse:

| Skill | What It Teaches the Agent |
|---|---|
| CLI tools | Use the Langfuse CLI for prompt management and export |
| Prompt migration | Migrate prompts between environments |
| API integration | Interact with Langfuse's REST API from agent code |

**Compatibility:** Claude Code, Cursor, Codex, Windsurf, and all [AgentSkills](https://agentskills.io/)-compatible tools.

> Set `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY` in your agent's environment settings.

---

## MCP

**Status:** ✅ Available

Langfuse provides an official MCP server (`mcp-server-langfuse`) that exposes prompt management as MCP tools — enabling agents and IDEs to list, fetch, create, and update prompts directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Docs** | https://langfuse.com/docs/api-and-data-platform/features/mcp-server |
| **MCP Repo** | https://github.com/langfuse/mcp-server-langfuse |
| **Transport** | StreamableHttp (native, no external setup) |
| **Endpoint** | `https://cloud.langfuse.com/api/public/mcp` |
| **Auth** | Basic Auth with base64-encoded project API keys |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Langfuse provides structured tracing for multi-step agent workflows. It captures the full execution trajectory of an agent — LLM calls, tool invocations, retriever steps, guardrail checks — organized in a typed, hierarchical trace structure. Production traces can be converted to evaluation datasets with one click, and OpenTelemetry integration allows existing monitoring infrastructure to receive agent telemetry.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Agent trajectory tracing — with semantic understanding of tool calls, memory reads, and reasoning steps — is the core product, not a bolt-on feature |
| **Agent-specific primitive** | Typed observation hierarchy (span → tool call → LLM call); dataset-based evaluation; trajectory replay; agent skill evaluation |
| **Autonomy-compatible control plane** | Passive, non-intrusive observation of autonomous agent execution |
| **M2M integration surface** | OpenTelemetry SDK, Python SDK, TypeScript SDK, native integrations with OpenAI Agents SDK, Claude SDK, LangChain |
| **Identity / delegation** | Per-run trace IDs; per-agent metadata; multi-agent attribution |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Typed Trace** | Hierarchical execution record: session → run → span → LLM call → tool call |
| **Tool Call Capture** | Structured record of tool name, input, output, latency, and cost |
| **Context Injection Tracking** | Which memories, retrieved documents, and system prompts were injected per LLM call |
| **Dataset-Based Evaluation** | Convert production traces to eval cases; measure accuracy, quality, and regression |
| **Trajectory Replay** | Reconstruct and inspect any agent's full execution path |
| **Cost Attribution** | Token usage and cost per agent run, per tool, per LLM call |
| **Agent Skill Evaluation** | Structured evaluation of specific agent capabilities across datasets |

---

## Trace Hierarchy

```
Session (user interaction or scheduled run)
  └── Trace (single agent run)
        └── Span (logical step)
              ├── LLM Call (prompt → completion + token counts)
              ├── Tool Call (name + input + output + latency)
              ├── Retriever Step (query + retrieved docs)
              └── Guardrail Check (input + policy + result)
```

Every level is captured with timing, token counts, costs, and metadata — not just a flat log.

---

## Autonomy Model

Langfuse is a **passive observer** — it captures what agents do without interfering. Agents instrument their code with the Langfuse SDK or use auto-instrumentation via OpenTelemetry. After that, all tracing is automatic.

---

## Identity and Delegation Model

- **Trace ID** — unique per agent run
- **Session ID** — groups runs for a single user interaction
- **User ID** — attributes runs to specific users
- **Metadata** — arbitrary key-value pairs for agent type, version, experiment name, etc.
- **Multi-agent** — nested traces support attribution in multi-agent architectures

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `langfuse.trace()`, `@observe()` decorator, context manager |
| TypeScript SDK | Equivalent TypeScript API |
| OpenTelemetry | OTEL-compatible; works with any OTEL-instrumented agent framework |
| OpenAI Agents SDK | Native auto-instrumentation |
| Claude SDK | Native auto-instrumentation |
| LangChain | Native callback integration |
| LangGraph | Native integration |

---

## Human-in-the-Loop Support

Tracing is passive. Humans review captured trajectories in the Langfuse UI for debugging, evaluation, and quality improvement. No human intervention is required during agent execution.

---

## Evaluation Workflow

```
Production traces (agent runs)
    ↓
Annotate traces with scores (human or LLM-as-judge)
    ↓
Convert traces to evaluation dataset (one click)
    ↓
Run evals against new prompt versions or model updates
    ↓
Compare quality metrics across versions
    ↓
Catch regressions in CI/CD before deployment
```

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Datadog** | Captures infrastructure metrics and generic logs; no semantic understanding of LLM calls, tool call structure, or agent reasoning |
| **CloudWatch** | Log aggregation for AWS services; no agent trajectory, no LLM token accounting |
| **Splunk** | Log search and SIEM; no agent-specific structure |
| **OpenTelemetry (alone)** | Telemetry standard; Langfuse is the backend that gives agent-specific meaning to OTEL traces |

---

## Use Cases

- **Debugging failed agent runs** — replay the exact trajectory to identify where reasoning went wrong
- **Prompt optimization** — compare agent quality across prompt versions using eval datasets
- **Cost optimization** — identify which tool calls and LLM calls are most expensive per task
- **Regression detection** — catch quality regressions when updating models or prompts in CI/CD
- **Multi-agent debugging** — trace execution across coordinated agent networks
- **Compliance** — maintain tamper-evident execution records for regulated agent deployments
