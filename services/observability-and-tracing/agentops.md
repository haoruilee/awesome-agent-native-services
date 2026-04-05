# AgentOps

> **"AgentOps is the developer favorite platform for testing, debugging, and deploying AI agents and LLM apps."**

| | |
|---|---|
| **Website** | https://www.agentops.ai |
| **Docs** | https://docs.agentops.ai |
| **GitHub** | https://github.com/AgentOps-AI/agentops |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social)](https://github.com/AgentOps-AI/agentops) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |

---

## Official Website

https://www.agentops.ai

---

## Official Repo

https://github.com/AgentOps-AI/agentops — OSS app + SDKs; cloud dashboard at AgentOps

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK auto-instrumentation` + **Public REST API** + **MCP docs helper**

1. **Python (minimal):**

```python
import agentops
agentops.init("<YOUR API KEY HERE>")
```

2. **Decorators** for custom workflows: `@trace`, `@agent`, `@tool` — see [Recording operations](https://docs.agentops.ai/v2/usage/recording-operations).
3. **Public API** (read traces/metrics): `https://api.agentops.ai` with JWT from API key — [Public API](https://docs.agentops.ai/v2/usage/public-api).
4. **MCP:** Mintlify docs MCP — `npx mint-mcp add agentops` per [introduction](https://docs.agentops.ai/) (IDE docs chat, not trace ingestion).

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add agentops/…` pack documented as primary.

```bash
npx clawhub@latest search agentops
```

---

## MCP

**Status:** ⚠️ **Docs MCP** for Mintlify (chat with documentation) — not a trace-ingestion MCP. Trace data flows through **SDK** and **REST**.

| Detail | Value |
|---|---|
| **Docs MCP** | `npx mint-mcp add agentops` |

---

## What It Does

AgentOps instruments **AI agents and LLM apps** with **sessions**, **waterfalls** of LLM/tool events, token/cost breakdowns, and **framework integrations** (LangChain, CrewAI, AutoGen, OpenAI Agents SDK, Google ADK, Smolagents, Haystack, AG2, etc.). It is explicitly positioned for **testing and debugging agents**, with a **public API** to pull trace data into other systems.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs intro: *"testing, debugging, and deploying AI agents and LLM apps"* — [docs.agentops.ai](https://docs.agentops.ai/) |
| **Agent-specific primitive** | **Session waterfall** of **tool calls + LLM calls**; `@agent` / `@tool` decorators; **multi-framework** agent hooks |
| **Autonomy-compatible control plane** | Passive instrumentation of autonomous runs |
| **M2M integration surface** | Python & TypeScript SDKs, **public REST API** for traces/metrics |
| **Identity / delegation** | API keys; project/session attribution for which agent run produced which spans |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | One agent run with timeline UI |
| **Waterfall** | Ordered LLM, tool, action, error events |
| **Trace decorators** | Explicit spans for custom code |
| **Public API** | Export traces for eval pipelines |
| **Framework auto-capture** | Zero/low config for major agent stacks |

---

## Autonomy Model

```
Agent process starts → agentops.init(key)
    ↓
Framework hooks record LLM + tool events automatically
    ↓
Dashboard + Public API consumers inspect trajectories
```

---

## Identity and Delegation Model

- **Project API keys** separate environments.
- **JWT** for Public API with rotation guidance (30-day tokens per docs summary).
- Sessions map to **agent runs** for audit.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install agentops` |
| TypeScript SDK | See docs |
| REST | `https://api.agentops.ai` |

---

## Human-in-the-Loop Support

Dashboard **session drilldown** and charts for human operators debugging agents.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Datadog / CloudWatch** | No **LLM + tool + prompt** semantic model |
| **Raw OpenTelemetry only** | No **agent session** UX and **framework-specific** auto hooks for agent stacks |

---

## Use Cases

- **Debug production agents** — See exactly which tool failed
- **Cost attribution** — Token usage per session
- **Eval export** — Pull traces via Public API
