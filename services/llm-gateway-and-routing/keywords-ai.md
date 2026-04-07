# Keywords AI

> **"AI gateway" — unified access to 250+ LLMs through a single API.**

| | |
|---|---|
| **Website** | https://www.keywordsai.co |
| **Docs** | https://docs.keywordsai.co |
| **GitHub** | N/A (hosted platform; integrate via OpenAI-compatible HTTP) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://www.keywordsai.co

---

## Official Repo

No primary open-source gateway repo — integration is **OpenAI-compatible** HTTP at `https://api.keywordsai.co` per [gateway quickstart](https://docs.keywordsai.co/get-started/quickstart/gateway).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `OpenAI-compatible REST` + **agent tracing**

1. Create account and **Keywords AI API key**.
2. Point the **OpenAI SDK** (or other supported clients) at Keywords AI base URL — see [chat completions](https://docs.keywordsai.co/api-endpoints/integration/chat-completions).
3. Configure **fallback models**, **load balancing**, **rate limits**, and **prompt management** in the dashboard per docs.
4. **OpenAI Agents SDK:** use `KeywordsAITraceProcessor` to send **agent traces** — [tracing docs](https://docs.keywordsai.co/integration/development-frameworks/tracing/openai-agents-sdk).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills registry entry documented here.

```bash
npx clawhub@latest search keywords ai
```

---

## MCP

**Status:** ⚠️ No first-party MCP server documented in this entry — agents integrate via **HTTP gateway** from tool code.

---

## What It Does

Keywords AI is an **AI gateway** for production LLM workloads: one endpoint routes to **many models**, adds **traffic management** (fallback, load balancing), **observability**, and **agent-aware tracing** when used with the OpenAI Agents SDK. It targets teams running **autonomous agents** that need reliability and cost control without forking provider SDKs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | First-class **OpenAI Agents SDK** tracing integration — [tracing](https://docs.keywordsai.co/integration/development-frameworks/tracing/openai-agents-sdk) |
| **Agent-specific primitive** | **KeywordsAITraceProcessor** for **multi-step agent** telemetry; gateway policies applied per **customer/user** in agent serving stacks |
| **Autonomy-compatible control plane** | Automatic **fallback** and **load balancing** without human failover |
| **M2M integration surface** | OpenAI-compatible **REST**, Python/TS/Go/PHP examples in docs |
| **Identity / delegation** | API keys; per-request **metadata** for user/session attribution (see gateway docs) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unified chat endpoint** | Single URL for 250+ models |
| **Fallback chain** | Model A → B on error or limit |
| **Load balancing** | Split traffic across providers |
| **Trace processor** | Agent run spans to Keywords AI |
| **Rate limits** | Protect agent fleets from runaway spend |

---

## Autonomy Model

```
Agent SDK → base URL api.keywordsai.co with Keywords API key
    ↓
Gateway applies routing, limits, fallbacks
    ↓
Provider response returned; traces recorded if processor attached
```

---

## Identity and Delegation Model

- **API keys** scope org access.
- **Per-end-user metadata** (when sent) supports multi-tenant agent apps.
- Rotate keys if an agent leaks credentials.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://api.keywordsai.co/api/chat/completions` |
| OpenAI SDK | Drop-in base URL swap |
| Agents SDK | `KeywordsAITraceProcessor` |

---

## Human-in-the-Loop Support

Dashboard for prompts, logs, and limits; runtime is automated.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Call OpenAI directly** | No **central fallback**, **multi-model** routing, or **agent trace processor** |
| **LiteLLM (see catalog entry)** | Keywords is a **hosted** product with **dashboard** governance for orgs; LiteLLM is **self-hosted OSS** with overlapping gateway features |

---

## Use Cases

- **Multi-agent SaaS** — One gateway for all tenants
- **Reliability** — Fallback when a provider degrades
- **Cost visibility** — Trace-linked usage for agent debugging
