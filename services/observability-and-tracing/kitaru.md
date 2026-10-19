# Kitaru

> **"Traces you can run, not just read."** — [zenml-io/kitaru README](https://github.com/zenml-io/kitaru)

| | |
|---|---|
| **Website** | https://www.zenml.io/product/kitaru |
| **Docs** | https://docs.zenml.io/kitaru |
| **GitHub** | https://github.com/zenml-io/kitaru |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/zenml-io/kitaru?style=social)](https://github.com/zenml-io/kitaru) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Apache 2.0 (open-source) |
| **Verified at** | 2026-10-19 |

---

## Official Website

https://www.zenml.io/product/kitaru

`https://kitaru.ai` redirects here. The product page titles Kitaru *"replay-based evals for AI agents"*.

---

## Official Repo

https://github.com/zenml-io/kitaru — Python/TypeScript SDKs, CLI, MCP server, framework adapters

---

## How to Use (Agent Onboarding)

**Quickest verified path** (from the [README](https://github.com/zenml-io/kitaru)):

```bash
uv add "kitaru[cli,worker,mcp]" kitaru-pydantic-ai    # or: pip install
kitaru login --local                                  # or: kitaru login <your-team-url>
npx skills add zenml-io/kitaru-skills
```

Then point an MCP client at `kitaru-mcp` per [Set up your coding agent](https://docs.zenml.io/kitaru/getting-started/setup). Docs: https://docs.zenml.io/kitaru

**Catalog note (2026-08-29):** earlier catalog copy described Kitaru as a durable-execution layer (`@flow` / `@checkpoint`). That positioning is obsolete. Live README and site describe replay-based evals over recorded or imported agent sessions.

---

## Agent Skills

**Status:** ✅ Official

```bash
npx skills add zenml-io/kitaru-skills
```

Upstream names a guided-tour skill and an investigation skill as the intended way to drive the record → replay → improve loop.

---

## MCP

**Status:** ✅ Available (`kitaru[mcp]` extra)

Docs: Kitaru is *"built to be driven by agents. The MCP server gives Claude Code, Codex, Cursor, and other coding assistants bounded Kitaru operations."* The CLI *"speaks JSON when a shell command is the right tool."*

| Detail | Value |
|---|---|
| **Install** | `uv add "kitaru[cli,worker,mcp]"` or `pip install "kitaru[mcp]"` |
| **Command** | `kitaru-mcp --server http://localhost:8000 --mode standard` (README example) |
| **Transport** | stdio |
| **Compatible Clients** | Claude Code, Codex, Cursor, any MCP-compatible client |

---

## What It Does

Kitaru records or imports production agent runs as **sessions**, then **replays** them against the agent's real code so a team can test a model, prompt, or code change against traffic that already happened. Tool calls are answered from the recording, so replay does not touch live systems.

The live README: *"Kitaru (来る, 'to arrive') gives you replay-based evals for AI agents."* The product page: *"Your agent's best eval data is already in production"* — turn traces into replayable evals.

The loop in docs: record or import → replay → improve (investigations, evaluators, cohorts, experiments). Kitaru sits **beside** an observability stack (Langfuse, LangSmith, Braintrust, Logfire, Arize Phoenix remain the system of record); it re-runs traces rather than replacing dashboards.

---

## Why It Is Agent-Native

The former durable-execution claim (`@flow` / `@checkpoint` as a long-running workflow runtime) is obsolete as of this freshness pass. The live product still qualifies on the **standard track** as an agent-eval / replay control plane — not generic ML experiment tracking.

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"Traces you can run, not just read"* and *"replay-based evals for AI agents"*. Docs: *"Kitaru is built to be driven by agents."* Product page: *"Kitaru by ZenML · Replay-based evals for AI agents"* |
| **Agent-specific primitive** | **Session** (one real agent run), **replay** against the agent's code with recorded tool answers, **cohorts** of production sessions, **evaluators** calibrated from human judgment of those runs, **experiments** that compare a change on the same cohort |
| **Autonomy-compatible control plane** | Import, replay, and experiment runs execute without a human clicking each step; coding-agent skills/MCP drive the investigation loop. Human judgment still authors eval criteria |
| **M2M integration surface** | Python SDK, TypeScript SDK, `kitaru` CLI (JSON), MCP server, official Agent Skills |
| **Identity / delegation** | Sessions are addressable records of a named agent (`agent_id` in adapters); experiments compare named runs; secrets and traces stay in the operator's environment (self-hosted by default) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | A replayable record of one real agent run (imported or recorded) |
| **Import** | Bring traces from Langfuse, LangSmith, Braintrust, Logfire, Arize Phoenix, or Kitaru JSONL |
| **Recording adapter** | One-line wrap for PydanticAI, OpenAI Agents SDK, LangGraph, Mastra, Vercel AI SDK |
| **Replay** | Re-execute the agent against the recorded world; tool calls answered from history |
| **Evaluator** | Criteria drafted from human judgments pinned to trace evidence |
| **Cohort** | A versioned set of production sessions used as a fixed test population |
| **Experiment** | Replay a cohort against one change (model, prompt, or working-tree code) and compare |

---

## Autonomy Model

```
Record with an adapter, or import existing traces
    ↓
Runs land as sessions (observability store stays system of record)
    ↓
Coding assistant investigates via skills + MCP; operator judges
    ↓
Evaluators and cohorts freeze the cases that matter
    ↓
kitaru experiment run replays the same cohort against a change
    ↓
Compare what improved and what broke before shipping
```

Replay answers tool calls from the recording. Production is not the test bench.

---

## Identity and Delegation Model

- Recording adapters take an `agent_id`; imported traces are tagged to an agent
- Each session is an addressable record of one run
- Self-hosted by default: server and workers run in the operator's infrastructure; traces do not have to leave that environment
- MCP exposes **bounded** operations to a coding assistant; the operator still owns judgments and paid/live replay decisions

---

## How Kitaru Differs from Generic Observability / Evals

Live FAQ on the product page: *"So is this an observability tool? No. It sits beside your observability stack. Traces tell you what happened; Kitaru re-runs them against your actual code."*

| Dimension | Kitaru | Langfuse / Braintrust / LangSmith |
|---|---|---|
| Role | Replay-based evals over real agent code | Trace store / dashboards / evals you read |
| Input | Import those tools' exports, or record with an adapter | Live production tracing |
| Test motion | Re-run the agent against a recorded world | Inspect spans; some evals score outputs without re-execution |
| Driver | CLI + MCP + Agent Skills for a coding assistant | Dashboards and SDKs |

This is why the catalog moved Kitaru from Durable Execution to Observability & Tracing (agent trajectories & evals). It is no longer a durable workflow runtime.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python / TypeScript SDK | Same server; adapters for PydanticAI, LangGraph, OpenAI Agents SDK, Mastra, Vercel AI SDK |
| CLI | `kitaru login`, `kitaru session import`, experiment/replay commands; JSON when a shell is the right tool |
| MCP | `kitaru-mcp` — bounded operations for coding assistants |
| Agent Skills | `npx skills add zenml-io/kitaru-skills` |
| Docs | https://docs.zenml.io/kitaru |

---

## Human-in-the-Loop Support

First-class for **eval criteria**, not for each replay step. Docs: the coding assistant interviews the operator over real sessions and pins judgments to trace evidence; those judgments calibrate evaluators. FAQ: evals change how much humans review, not whether they do.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic APM / log dashboards** | Request latency and error rates; no agent-session replay against real agent code |
| **Trace stores alone** | Official FAQ: they tell you what happened; they do not re-run the agent |
| **Offline golden-set eval harnesses** | Synthetic prompts, not production sessions imported as replayable agent runs |
| **Durable workflow engines** | Checkpoint/retry for jobs; not replay-based evals over agent traces (Kitaru's former catalog claim) |

---

## Use Cases

- **Regression gates** — replay the cohort that caught a failure on every commit
- **Model swap** — same cohort, one model changed; review only the sessions that differ
- **Import-first adoption** — start from Langfuse/LangSmith/Braintrust/Logfire/Phoenix exports with no production code change
- **Coding-agent investigation** — skills + MCP walk an operator through evidence before creating resources or starting paid replay
