# LiteLLM

> **"AI Gateway to provide model access, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format."**

| | |
|---|---|
| **Website** | https://www.litellm.ai |
| **Docs** | https://docs.litellm.ai |
| **GitHub** | https://github.com/BerriAI/litellm |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social)](https://github.com/BerriAI/litellm) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://www.litellm.ai

---

## Official Repo

https://github.com/BerriAI/litellm

---

## How to Use (Agent Onboarding)

**Self-hosted proxy — OpenAI-compatible gateway with virtual keys, budgets, and agent routing.**

```bash
pip install litellm
# Deploy proxy per https://docs.litellm.ai/docs/proxy/docker_quick_start
# Point OpenAI SDK base_url at your LiteLLM proxy (e.g. http://localhost:4000)
```

**Agent Gateway (A2A)** — onboard A2A-compatible agents (Vertex Agent Engine, Bedrock AgentCore, LangGraph, Pydantic AI, etc.) and invoke via A2A or OpenAI-style `a2a/` model prefix — see [Agent Gateway (A2A)](https://docs.litellm.ai/docs/a2a).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills repo located; search community:

```bash
npx clawhub@latest search litellm
```

---

## MCP

**Status:** ✅ LiteLLM documents **MCP** integration on the AI Gateway (pass-through / proxy patterns for MCP servers — see [docs index](https://docs.litellm.ai/docs/) and search "MCP"). Treat as gateway feature rather than a single stdio package name.

---

## What It Does

LiteLLM is an **open-source AI gateway** that unifies **100+ LLM providers** behind an **OpenAI-compatible** API. Platform teams use it for **virtual keys**, **spend tracking**, **budgets**, **rate limits**, **fallbacks**, **guardrails**, and **logging** (Langfuse, OpenTelemetry, etc.). The **Agent Gateway** adds first-class **A2A (Agent-to-Agent)** routing, **iteration budgets**, **trace grouping** (`X-LiteLLM-Trace-Id`), and **per-agent spend** (`X-LiteLLM-Agent-Id`) for multi-step agents — see [A2A docs](https://docs.litellm.ai/docs/a2a).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Dedicated **Agent Gateway** docs for A2A, Bedrock AgentCore, Vertex Agent Engine, LangGraph, Pydantic AI; OpenAI SDK integration with `a2a/` prefix |
| **Agent-specific primitive** | **A2A JSON-RPC** endpoints; **iteration budgets** for agent loops; **headers for trace grouping and agent spend attribution** across nested LLM calls |
| **Autonomy-compatible control plane** | Automatic **fallbacks**, **load balancing**, and **budget enforcement** at the proxy — agents need not implement provider-specific retry matrices |
| **M2M integration surface** | Python package, **Docker / Helm** proxy deployment, Admin UI, REST APIs |
| **Identity / delegation** | **Virtual keys** scoped to teams/users/tags; spend reports per key/user/team |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **OpenAI-compatible proxy** | Single `/v1` surface for many providers |
| **Virtual keys** | Scoped credentials with budgets and RBAC (Enterprise features) |
| **Agent Gateway / A2A** | Register and invoke A2A agents; optional OpenAI SDK path |
| **Trace / agent headers** | Propagate `X-LiteLLM-Trace-Id` and `X-LiteLLM-Agent-Id` for cost and trace grouping |
| **Iteration budgets** | Cap agent loop iterations at the gateway |
| **Guardrails & logging** | Policy hooks; export to OTEL, S3, Langfuse, etc. |

---

## Autonomy Model

```
Agent or orchestrator sends requests to LiteLLM proxy with virtual key
    ↓
Proxy enforces budget / rate limits → routes to provider or A2A agent
    ↓
On failure → configured fallback model or provider
    ↓
Logs and metrics capture latency, cost, and (with headers) full agent trace
```

---

## Identity and Delegation Model

- **Virtual keys** map to teams/users and budget policies.
- **A2A forwarding** supports **agent identity** via LiteLLM headers for nested calls back through the proxy.
- **Audit** via proxy logs, enterprise SSO, and export sinks (per enterprise docs).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP | OpenAI-compatible chat/completions on proxy |
| A2A | `POST /a2a/{agent_name}/message/send` — see docs |
| Python | `pip install litellm` |
| Deploy | Docker, Kubernetes — see [proxy deploy](https://docs.litellm.ai/docs/proxy/deploy) |

---

## Human-in-the-Loop Support

Long-running A2A flows may support human input (Temporal-backed patterns in related stacks); LiteLLM core is policy and routing infrastructure.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Direct provider APIs** | No unified fallback, cross-provider budgets, or A2A registry in one layer |
| **NGINX / API gateway** | No LLM cost accounting, semantic guardrails, or A2A agent routing |
| **Single-cloud router** | Vendor-locked; LiteLLM spans OpenAI, Anthropic, Bedrock, Azure, Gemini, etc. |

---

## Use Cases

- **Agent fleets** — attribute spend and traces per agent ID across many LLM calls
- **Model abstraction** — swap providers without changing agent SDK code
- **On-prem / VPC** — self-host gateway for compliance while keeping OpenAI SDK ergonomics
