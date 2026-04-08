# Braintrust

> **"Ship quality AI at scale"** — AI observability and evaluation.

| | |
|---|---|
| **Website** | https://www.braintrust.dev |
| **Docs** | https://www.braintrust.dev/docs |
| **GitHub** | https://github.com/braintrustdata/autoevals |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/braintrustdata/autoevals?style=social)](https://github.com/braintrustdata/autoevals) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |

---

## Official Website

https://www.braintrust.dev

---

## Official Repo

https://github.com/braintrustdata/autoevals — open-source eval scorers (companion to Braintrust platform)

https://github.com/braintrustdata/braintrust-sdk-python — Python SDK

Additional SDKs and tooling under https://github.com/braintrustdata

---

## How to Use (Agent Onboarding)

**SDK — trace production agents and run evals; MCP for IDE-integrated access.**

```bash
pip install "braintrust[openai-agents]"
```

**OpenAI Agents SDK** — use `BraintrustTracingProcessor` — see [OpenAI Agents SDK integration](https://www.braintrust.dev/docs/integrations/agent-frameworks/openai-agents-sdk).

**MCP (HTTP)** — add Braintrust MCP to your coding agent host:

```bash
claude mcp add --transport http braintrust https://api.braintrust.dev/mcp \
  --header "Authorization: Bearer $BRAINTRUST_API_KEY"
```

See [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) and [MCP reference](https://www.braintrust.dev/docs/reference/mcp). EU data plane: `https://api-eu.braintrust.dev/mcp`.

---

## Agent Skills

**Status:** ⚠️ No single `npx skills add` bundle verified; MCP exposes logs, evals, and prompt workflows to compatible hosts.

---

## MCP

**Status:** ✅ Hosted MCP endpoint for coding agents and IDEs.

| Detail | Value |
|---|---|
| **MCP Docs** | https://www.braintrust.dev/docs/integrations/developer-tools/mcp |
| **Endpoint (US)** | `https://api.braintrust.dev/mcp` |
| **Endpoint (EU)** | `https://api-eu.braintrust.dev/mcp` |
| **Auth** | `Authorization: Bearer` API key or OAuth per docs |

---

## What It Does

Braintrust is an **AI observability and evaluation** platform: **trace** every LLM call, tool invocation, and intermediate step in production; **score** outputs with code, LLM judges, or humans; **compare** prompts and models; and **convert traces to datasets** for regression testing. It explicitly targets **agents** — e.g. native **OpenAI Agents SDK** trace processors — and exposes an **MCP server** so coding agents can query experiments and logs directly.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: AI fails differently — *"trace everything"* including **tool calls**; first-class **OpenAI Agents SDK** integration docs |
| **Agent-specific primitive** | **Trace hierarchy for tool + LLM spans**; **Eval** tasks that take an **agent `Runner`** as the unit under test; **trace → dataset** for replay |
| **Autonomy-compatible control plane** | Instrumentation runs in the agent process; scoring can be automated (CI or online) |
| **M2M integration surface** | Python/TS/Go/Ruby/C# SDKs; **MCP**; API |
| **Identity / delegation** | **Projects**, **API keys**, **RBAC**, **audit-friendly** logging; hybrid / self-hosted data plane options |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Trace** | Nested spans for LLM, tool, retriever, and custom steps |
| **Eval / Experiment** | Datasets + scorers + comparisons across prompts/models |
| **Trace processors** | e.g. `BraintrustTracingProcessor` for OpenAI Agents |
| **MCP tools** | Query logs, run evals, manage prompts from the IDE |
| **Brainstore** | Storage engine optimized for large nested AI traces |

---

## Autonomy Model

```
Agent code initializes Braintrust logger + trace processor
    ↓
Each LLM/tool step emits spans with inputs, outputs, latency, cost
    ↓
Dashboards and alerts surface regressions; optional online eval sampling
    ↓
Failed traces become dataset rows for offline regression tests
```

---

## Identity and Delegation Model

- **API keys** scope access to org/project data.
- **RBAC** controls who can view traces with potentially sensitive prompts.
- **Hybrid deployment** keeps data plane in customer infrastructure when required.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install braintrust` / `braintrust[openai-agents]` |
| TypeScript SDK | `@braintrust/*` packages per docs |
| MCP | HTTPS `api.braintrust.dev/mcp` |
| REST API | https://www.braintrust.dev/docs/api-reference/introduction |

---

## Human-in-the-Loop Support

**Human scoring** and **annotation UIs** for evals; **Loop** assistant helps authors iterate on prompts and scorers.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic APM (Datadog)** | No first-class LLM/tool span model or prompt-diff workflows |
| **Log-only stacks** | No eval loops, datasets, or MCP bridge for coding agents |
| **Notebook-only testing** | No production trace ingestion at scale |

---

## Use Cases

- **Agent debugging** — find which tool call derailed a long chain
- **CI eval gates** — block releases when scorers regress on golden sets
- **Model upgrades** — compare traces side-by-side across model versions
