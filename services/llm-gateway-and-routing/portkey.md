# Portkey

> **"The AI gateway built for production agents."**

| | |
|---|---|
| **Website** | https://portkey.ai |
| **Docs** | https://portkey.ai/docs |
| **GitHub** | https://github.com/Portkey-AI/portkey-python-sdk |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **Compliance** | SOC 2 · ISO 27001 |
| **Scale** | 3,000+ GenAI teams · 1,600+ LLMs · 1M rpm throughput |

---

## Official Website

https://portkey.ai

---

## Official Repo

https://github.com/Portkey-AI/portkey-python-sdk — Python SDK

https://github.com/Portkey-AI/portkey-node-sdk — Node.js SDK

---

## Agent Skills

**Status:** ⚠️ No official skill published by Portkey yet.

```bash
npx clawhub@latest search portkey
```

---

## MCP

**Status:** ⚠️ No dedicated MCP server published.

Portkey integrates with all major agent frameworks (OpenAI Agents SDK, LangChain, CrewAI, AutoGen, LlamaIndex) via an OpenAI-compatible REST API — agents point their LLM client at Portkey's gateway instead of the provider directly.

---

## What It Does

Portkey is an AI gateway that sits between agent code and LLM providers. Agents send requests to Portkey's OpenAI-compatible endpoint; Portkey handles routing, fallback, caching, budget enforcement, and observability — transparently, without the agent needing to know which underlying provider is serving the request.

The key primitives are specifically designed for agent workloads: **virtual keys** (per-agent scoped credentials), **per-agent budget limits**, **sticky session routing** (keep the same agent on the same provider during a multi-turn conversation), and **agent-trace observability** (trace multi-hop agent call chains with cost attribution per step).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Portkey's agents page: *"Bring Your Agents to Prod"*; dedicated agent integration docs for all major frameworks; agent observability positioned as the core product |
| **Agent-specific primitive** | Per-agent virtual keys; per-agent budget limits with alerts; sticky session routing for multi-turn agents; agent trace IDs linking multi-step chains; semantic caching for repeated agent queries |
| **Autonomy-compatible control plane** | Automatic fallback across providers; agents never see a provider failure — Portkey retries and reroutes transparently |
| **M2M integration surface** | OpenAI-compatible REST API (drop-in replacement); Python SDK; Node SDK; 2-line integration for all major frameworks |
| **Identity / delegation** | Virtual keys scoped per agent/project; per-request metadata for agent attribution; budget policies scoped by API key or metadata |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Virtual Key** | Scoped proxy credential per agent/project — real provider key never exposed in agent code |
| **Per-Agent Budget Limit** | USD or token-based spending cap per virtual key with alert thresholds |
| **Automatic Fallback** | If primary provider fails or rate-limits, route to backup provider automatically |
| **Sticky Session Routing** | Keep a multi-turn agent conversation on the same provider instance |
| **Semantic Cache** | Return cached responses for semantically similar queries, reducing cost |
| **Agent Trace** | Link all LLM calls in a multi-step agent chain under a single trace ID |
| **Load Balancing** | Distribute requests across providers with weighted or round-robin strategies |
| **Guardrails** | Validate inputs and outputs against policy rules before/after LLM calls |

---

## Autonomy Model

```
Agent code points LLM client at Portkey endpoint (2-line change)
    ↓
Agent sends request with virtual key + optional trace metadata
    ↓
Portkey checks budget → applies cache → routes to provider
    ↓
If provider fails: automatic fallback to configured backup
    ↓
Response returned to agent — provider identity is transparent
    ↓
All calls logged with cost, tokens, latency, trace ID
```

Agents never change code when providers fail, rate-limit, or are replaced.

---

## Identity and Delegation Model

- **Virtual keys** — each agent gets its own scoped credential; real API keys stored by Portkey, never in agent code
- **Budget policies** — scoped by virtual key, metadata tag, or workspace; alerts before exhaustion
- **Trace IDs** — every multi-step agent chain has a trace ID linking all LLM calls for cost and debugging attribution
- **Workspace isolation** — separate budget, keys, and logs per project or team

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | OpenAI-compatible endpoint: `https://api.portkey.ai/v1` |
| Python SDK | `pip install portkey-ai` |
| Node SDK | `npm install portkey-ai` |
| Framework Support | OpenAI Agents SDK, LangChain, CrewAI, AutoGen, LlamaIndex, LangGraph — 2-line integration |
| LLM Coverage | 1,600+ models across 200+ providers |

---

## Human-in-the-Loop Support

Not applicable as a core primitive. Portkey is infrastructure — HITL is composed at the agent application layer. Budget alerts can notify humans when agent spending approaches limits.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Direct OpenAI/Anthropic API** | No fallback, no per-agent budget, no cross-provider routing, no agent trace linking |
| **LiteLLM (self-hosted)** | Open-source proxy without managed per-agent budget enforcement, enterprise security, or agent-specific trace primitives |
| **AWS Bedrock (routing)** | AWS-vendor-locked; no per-agent virtual keys, no cross-cloud fallback |
| **API gateway (Kong, NGINX)** | Generic HTTP proxies; no LLM-specific primitives, no semantic caching, no agent trace |

---

## Use Cases

- **Multi-provider agents** — agent uses GPT-4o as primary, Claude Sonnet as fallback; Portkey handles failover transparently
- **Cost-controlled agent fleets** — each agent deployment gets a virtual key with a USD budget cap; spend reported per agent
- **Debugging multi-hop chains** — trace ID links all 20+ LLM calls in a complex research agent for cost and latency attribution
- **A/B testing models** — route 10% of agent traffic to a new model to compare quality before full cutover
- **Compliance deployments** — Portkey on-prem or VPC ensures no agent traffic leaves the corporate network
