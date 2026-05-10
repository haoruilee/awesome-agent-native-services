# Laminar

> **"Open-source observability platform for long-running agents. Trace in one line, debug from any step, detect patterns at scale."**

| | |
|---|---|
| **Website** | https://laminar.sh |
| **Docs** | https://laminar.sh/docs |
| **GitHub** | https://github.com/lmnr-ai/lmnr |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing](README.md) |
| **License** | Apache 2.0 (self-host) · Y Combinator-backed · $3M seed (March 2026) |
| **Stars** | 2,800+ |

---

## Official Website

https://laminar.sh

---

## Official Repo

https://github.com/lmnr-ai/lmnr

---

## How to Use (Agent Onboarding)

```
# Self-host:
git clone https://github.com/lmnr-ai/lmnr
cd lmnr && docker compose up -d

# Or hosted: sign up at laminar.sh

# Two lines to integrate:
from lmnr import Laminar
Laminar.initialize()
```

Auto-instruments common AI frameworks and SDKs.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an official skill.

```bash
npx clawhub@latest search laminar
```

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server. Laminar's data plane is OpenTelemetry-compatible; tracing is integrated via the SDK.

| Detail | Value |
|---|---|
| **Transport** | OTLP / SDK |
| **Compatible Clients** | Browser Use, Stagehand, Playwright, Kernel, Browserbase, OpenAI Agents SDK, custom |

---

## What It Does

Laminar is an agent-native observability platform. Where conventional LLM observability tools (Langfuse, LangSmith) optimize for **prompt → completion** pairs, Laminar's data model is **agent-trace-first**: thousands of spans, non-deterministic control flow, nested causality, and session continuity are first-class.

Five capabilities define the product:

1. **One-line tracing** for popular AI frameworks and SDKs.
2. **True agent debugger** — local agent runs visible in the browser; rerun at step N with previous context preserved; tune system prompts and reflect changes instantly.
3. **Browser-agent session replay** — automatic capture and sync with traces (Browser Use, Stagehand, Playwright, Kernel, Browserbase).
4. **Signals** — describe an event in natural language; Laminar extracts it from past and future traces (e.g., "agent failure due to logic error"), with a defined output schema and email/Slack reports.
5. **SQL over traces** — query the entire trace corpus with SQL; feed Evals datasets straight from a query.

Self-host is fully Apache 2.0; the platform is written in Rust and aimed at terabyte-scale trace data.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Open-source observability platform for long-running agents."* |
| **Agent-specific primitive** | Agent debugger that reruns at step N with preserved context, browser-agent session replay, Signals (NL → trace pattern detector) |
| **Autonomy-compatible control plane** | Tracing is non-blocking; agents run unchanged; no per-action human approval |
| **M2M integration surface** | OTLP + SDK (Python, TS) + SQL API + REST |
| **Identity / delegation** | Trace + span IDs; metadata tags per agent / user / session |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Trace** | Hierarchical, multi-thousand-span trace optimized for long agent runs |
| **Step Replay** | Rerun an agent at step N with the original upstream context preserved |
| **Browser Session Replay** | Automatic screen capture synced with the trace |
| **Signals** | NL-defined event detector that runs over past and future traces |
| **SQL API** | Query traces directly; feed datasets for Evals |
| **Evals** | Define dataset + executor + scoring metric; first-class in the platform |

---

## Autonomy Model

1. Agent runs anywhere (local, cloud, sandbox).
2. Two-line SDK init forwards spans to Laminar (OTLP).
3. Operator opens any trace in the browser; full context is preserved.
4. To debug: pick a step, mutate the system prompt, rerun from there.
5. To analyze at scale: define a Signal in NL ("agent failure with `logic_error`"); Laminar extracts events from millions of traces.

---

## Identity and Delegation Model

- Trace ID + span ID + agent ID + session ID metadata.
- Per-trace authorship attribution; teams can scope visibility.
- Datasets derived from SQL queries inherit trace identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| OTLP | Native OpenTelemetry receiver |
| Python SDK | `pip install lmnr` |
| TypeScript SDK | `npm install @lmnr-ai/lmnr` |
| SQL API | Query traces directly |
| Evals SDK | `evaluate({ data, executor, evaluators, config })` |
| Self-host | Docker Compose / Helm |

---

## Human-in-the-Loop Support

Observability platform; HITL is out of scope. Composes naturally with HumanLayer / Inferable: HITL events show up as spans in the trace.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Langfuse** | Prompt/completion-shaped data model; less ergonomic for thousand-span agent traces |
| **LangSmith** | LangChain/LangGraph-centric; closed-source; per-seat pricing |
| **Plain OTel + Grafana** | Generic — no agent debugger, no step rerun, no NL Signals, no browser session replay |

---

## Use Cases

- **Long-running agent debugging** — open a failed run, jump to the step that broke, rerun with a tweaked prompt
- **Browser-agent QA** — replay an entire Browser Use / Stagehand / Browserbase session synced with the LLM trace
- **Trace-corpus analysis** — Signals turns "find all the times the agent confused tools" into a one-shot query
- **CI Evals** — pull a dataset from SQL over yesterday's traces, run evals before deploying a new prompt
