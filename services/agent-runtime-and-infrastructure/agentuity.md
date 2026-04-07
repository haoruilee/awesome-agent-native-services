# Agentuity

> **"The Full-Stack Platform for AI Agents."**

| | |
|---|---|
| **Website** | https://agentuity.com |
| **Docs** | https://agentuity.dev |
| **GitHub** | https://github.com/agentuity/sdk |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agentuity/sdk?style=social)](https://github.com/agentuity/sdk) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://agentuity.com

---

## Official Repo

https://github.com/agentuity/sdk — TypeScript / platform SDK

https://github.com/agentuity/sdk-py — Python SDK

https://github.com/agentuity/cli — CLI

---

## How to Use (Agent Onboarding)

**SDK / REST — create and deploy agents with built-in storage, sandboxes, and observability.**

```bash
# Follow quickstart at https://agentuity.dev — install CLI and SDK, then deploy.
# Example pattern (see official docs for current commands):
npm install @agentuity/sdk
```

Agentuity wraps existing agent frameworks (e.g. Vercel AI SDK, Mastra) with production routing, evals, streaming, and cross-agent calls without forcing a new agent authoring model — see [Creating agents](https://agentuity.dev/agents/creating-agents).

---

## Agent Skills

**Status:** ⚠️ No official `SKILL.md` registry entry located yet.

```bash
npx clawhub@latest search agentuity
```

---

## MCP

**Status:** ⚠️ No dedicated MCP server documented as a first-class product surface.

---

## What It Does

Agentuity is a deployment and runtime platform for **AI agents as workloads**: type-safe APIs and optional React frontends, **Postgres / Redis / vector / object storage** exposed to agents as tools, **ephemeral sandboxes** for untrusted code, **OpenTelemetry**-based observability (prompts, responses, cost per span), **evals** tied to production traffic, and **I/O** integrations (email, SMS, webhooks, cron). It targets **long-running, session-oriented agent execution** rather than classic stateless HTTP services — see [AI agent infrastructure](https://agentuity.com/ai-agent-infrastructure) and related architecture guides on the marketing site.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage and product copy center **AI agents** as the primary workload — *"The Full-Stack Platform for AI Agents"*; guides on agent runtime, deployment, and multi-agent orchestration |
| **Agent-specific primitive** | **Agent sandboxes** (create / run / destroy untrusted code in one call); **agent evals** on live traffic; **session-level observability** spanning prompts, tools, and cost — not generic APM alone |
| **Autonomy-compatible control plane** | Agents run through APIs and automated deploys (e.g. Git push); budgets and policies are platform concerns, not per-click human approval for each model call |
| **M2M integration surface** | SDKs (JS/TS, Python), CLI, HTTP APIs, OpenTelemetry export |
| **Identity / delegation** | Authentication, rate limiting, and API design are built for **programmatic** agent and app access; org/project scoping for keys and resources (per docs) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent runtime** | `createAgent`-style handlers with schema, streaming, and framework interop |
| **Sandboxes** | Isolated containers for untrusted agent-generated code with managed lifecycle |
| **Storage tools** | Redis, Postgres, vector, and object storage reachable from agent context |
| **Observability** | OTel traces, logs, and session debugging tuned to LLM spans |
| **Evals** | Evaluations deployed with agents against production-shaped traffic |
| **I/O & scheduling** | Webhooks, cron, messaging channels as agent inputs/outputs |

---

## Autonomy Model

```
Developer defines agent handler + schema in code
    ↓
CLI / CI deploys to Agentuity edge — SSL, DNS, load balancing managed
    ↓
Agent receives requests; may use storage, sandboxes, and external I/O via APIs
    ↓
OTel + evals capture trajectories and quality signals without manual log scraping
    ↓
Multi-agent calls use platform primitives instead of ad-hoc service discovery
```

---

## Identity and Delegation Model

- **API keys and auth** scoped to projects/workspaces (per platform docs).
- **Sandboxes** isolate execution so one agent run cannot read another's filesystem.
- **Traces** attribute usage and cost to sessions/spans for audit and tuning.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `@agentuity/sdk` — see GitHub |
| Python SDK | `agentuity` — see GitHub |
| CLI | `agentuity` CLI — see GitHub |
| HTTP / Webhooks | Product I/O and API routes — see https://agentuity.dev |

---

## Human-in-the-Loop Support

Evals and observability support human review of traces and scores; core execution does not require a human in the request path.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Kubernetes + Lambda** | No first-class agent session model, sandbox lifecycle, or LLM-native evals on live traffic without heavy custom build |
| **PaaS (Heroku, Cloud Run)** | General web workloads; no bundled agent storage toolkit, OTel-first LLM spans, or agent eval product |
| **Notebook / batch only** | No production agent routing, global edge deploy, or multi-agent call semantics |

---

## Use Cases

- **Production agents** — deploy Mastra / AI SDK agents with managed infra and tracing
- **Tool-heavy agents** — combine DB, object store, and vector search from one platform
- **Unsafe code execution** — run generated code in disposable sandboxes
- **Quality loops** — ship evals that run on real traffic, not only offline datasets
