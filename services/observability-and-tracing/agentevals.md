# AgentEvals

> **"Ship Agents Reliably — Benchmark your agents before they hit production. AgentEvals scores performance and inference quality from OpenTelemetry traces — no re-runs, no guesswork."**

| | |
|---|---|
| **Website** | https://aevals.ai |
| **Docs** | https://aevals.ai/docs/ |
| **GitHub** | https://github.com/agentevals-dev/agentevals |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agentevals-dev/agentevals?style=social)](https://github.com/agentevals-dev/agentevals) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Open-source (see repository) |

---

## Official Website

https://aevals.ai

---

## Official Repo

https://github.com/agentevals-dev/agentevals — CLI, OTLP receiver, web UI, REST API, MCP server, Helm chart

Community evaluator registry: https://github.com/agentevals-dev/evaluators

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + **OpenTelemetry** + optional **MCP** + **live OTLP receiver**

1. Install:

```bash
pip install agentevals-cli
```

Optional: `pip install "agentevals-cli[live]"` for MCP server support.

2. Score a trace file against a golden eval set:

```bash
agentevals run samples/helm.json \
  --eval-set samples/eval_set_helm.json \
  -m tool_trajectory_avg_score
```

3. **Zero-code live dev:** run `agentevals serve --dev`, then point your agent’s OTLP exporter at the bundled receiver (e.g. `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318`) — see [README — Use-cases and integrations](https://github.com/agentevals-dev/agentevals/blob/main/README.md).

4. **MCP:** with `[live]` extra, run `agentevals mcp` — exposes tools such as `evaluate_traces`, `list_metrics`, and (when server is running) session evaluation tools — see [MCP Server](https://github.com/agentevals-dev/agentevals/blob/main/README.md#mcp-server).

---

## Agent Skills

**Status:** ⚠️ No standalone `npx skills add …` pack; the upstream repo documents Claude Code slash workflows under `.claude/skills/` for **repository contributors**, not a published ClawHub skill.

```bash
npx clawhub@latest search agentevals
```

---

## MCP

**Status:** ✅ Available (ships with `agentevals-cli[live]`)

| Detail | Value |
|---|---|
| **MCP Docs** | [README — MCP Server](https://github.com/agentevals-dev/agentevals/blob/main/README.md#mcp-server) |
| **Transport** | Streamable HTTP (default port **8080** when running the bundled deployment image / `serve`) |
| **Tools (examples)** | `list_metrics`, `evaluate_traces`, `list_sessions`, `summarize_session`, `evaluate_sessions` |
| **Compatible Clients** | Claude Code (`.mcp.json` auto-discovery documented upstream), Cursor, any MCP client |

---

## What It Does

AgentEvals scores **AI agent behavior** from **OpenTelemetry traces** without re-executing the agent. It ingests OTLP or Jaeger JSON, compares runs against **golden eval sets** (expected tool trajectories, responses), and reports pass/fail metrics suitable for CI. A bundled web UI and OTLP receiver support live streaming during development; Kubernetes Helm chart and Docker image support production-adjacent deployment next to agent workloads.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product copy centers on **agents**: *"Benchmark your **agents** before they hit production"* and *"Evaluate **agent behavior** from real traces"* — [aevals.ai](https://aevals.ai/) |
| **Agent-specific primitive** | **Trace-based tool trajectory matching** (`tool_trajectory_avg_score`), golden eval sets for expected tool calls, trajectory match modes (e.g. strict / order-relaxed) — behaviors meaningless for non-agent apps |
| **Autonomy-compatible control plane** | Passive evaluation of autonomous runs; **no re-run** requirement — scores existing telemetry |
| **M2M integration surface** | CLI (`agentevals run`), REST/Swagger with `serve`, OTLP HTTP/gRPC ingestion, **MCP tools**, Helm/Docker |
| **Identity / delegation** | Traces carry OTel **session** / **resource** attributes (e.g. `agentevals.session_name`, `agentevals.eval_set_id` per upstream README); eval results attributable to trace IDs and sessions |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Golden Eval Set** | JSON definition of expected agent behavior (tools, responses) |
| **Trajectory Matching** | Compare actual tool spans to expected sequences — multiple match policies |
| **OTLP / Jaeger Ingest** | Evaluate production or test traces without proprietary lock-in |
| **Built-in Metrics** | e.g. `tool_trajectory_avg_score`, `response_match_score`; LLM-as-judge option |
| **Custom Evaluators** | User-defined scorers (Python, JS, or stdin/stdout protocol) |
| **Live Session Streaming** | `agentevals serve` + OTLP endpoint for real-time span inspection |
| **MCP Evaluation Tools** | Run metrics and session summaries from an MCP client |

---

## Autonomy Model

```
Instrumented agent emits OpenTelemetry spans (tools, LLM, retrievers)
    ↓
Traces land in agentevals (file, OTLP receiver, or exported JSON)
    ↓
CLI or MCP runs evaluators against golden eval sets
    ↓
Pass/fail + scores returned for CI gates or human review — no second agent invocation required
```

---

## Identity and Delegation Model

- **Trace ID** and span hierarchy identify a single agent run
- **Session grouping** via OTel resource attributes (`agentevals.session_name` documented in upstream README)
- **Eval set binding** via `agentevals.eval_set_id` for associating streams with expected behavior definitions
- Evaluator outputs are machine-readable (JSON / CLI tables) for automated policy gates

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `agentevals run`, `agentevals serve`, `agentevals mcp`, `agentevals evaluator list` |
| OTLP | HTTP receiver on **4318** (and gRPC **4317** patterns via Collector) — see upstream README |
| REST API | Embedded in `serve` — `/docs`, `/redoc` |
| MCP | Port **8080** in containerized deployment — [README](https://github.com/agentevals-dev/agentevals/blob/main/README.md) |
| Kubernetes | Helm chart in `charts/agentevals/` |

---

## Human-in-the-Loop Support

Optional human review via the **Web UI** for trace inspection and score interpretation. No human is required for CLI-based CI gating.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic APM (Datadog, etc.)** | Infrastructure metrics and logs — no first-class **golden tool trajectory** eval sets for agents |
| **Dataset-only eval platforms that re-run code** | Burn tokens replaying LLMs; agentevals emphasizes **scoring without re-execution** |
| **Langfuse / AgentOps** | Listed separately — full observability stacks; agentevals focuses on **OTel-trace-driven eval** with MCP + local-first operation |

---

## Use Cases

- **CI gates** — fail builds when tool trajectories diverge from golden references
- **Regression testing across models** — same eval sets, different provider traces
- **Live dev debugging** — stream OTel into `serve` and inspect tool chains in the UI
- **MCP-driven review** — trigger `evaluate_traces` from a coding agent session
