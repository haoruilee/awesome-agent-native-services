# Respan (Keywords AI)

> **"Route, observe, and evaluate every LLM call"**

| | |
|---|---|
| **Website** | https://www.respan.ai/ |
| **Docs** | https://www.respan.ai/docs/documentation/overview |
| **GitHub** | N/A (hosted platform; integrate via OpenAI-compatible HTTP) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **Verified at** | 2026-08-29 |

---

## Official Website

https://www.respan.ai/

Title: *Respan | LLM Engineering Platform*. [About](https://www.respan.ai/about) still says *Respan (formerly Keywords AI)*. Rebrand post: [Announcing our new brand: Respan](https://www.respan.ai/blog/introducing-respan) (“Today, Keywords AI is officially rebranded as Respan.”). Old site `https://www.keywordsai.co` is no longer the official homepage.

---

## Official Repo

No primary open-source gateway repo — integration is **OpenAI-compatible** HTTP. Live gateway host: https://api.respan.ai/ (`{"status":"ok"}`). SDK/docs still use base URL `https://api.respan.ai/api` ([AI Gateway](https://www.respan.ai/ai-gateway), [provider inference docs](https://www.respan.ai/docs/integrations/gateway/model-providers/inference.md)). `https://api.keywordsai.co` still returned HTTP 200 on 2026-08-29; prefer the Respan host the current docs publish.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `OpenAI-compatible REST` + **agent tracing**

1. Create an account at [platform.respan.ai](https://platform.respan.ai) and a **Respan API key**.
2. Point the SDK you already use at `https://api.respan.ai/api` — see [AI Gateway](https://www.respan.ai/ai-gateway) and [docs overview](https://www.respan.ai/docs/documentation/overview).
3. Configure fallbacks, caching, and spend limits per docs.
4. **OpenAI Agents SDK:** use `OpenAIAgentsInstrumentor` with `Respan(...)` — [tracing docs](https://www.respan.ai/docs/integrations/openai-agents-sdk).

Former Keywords AI doc paths (`docs.keywordsai.co/get-started/quickstart/gateway`, `…/chat-completions`) 404 after redirect.

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills registry entry documented here.

```bash
npx clawhub@latest search respan
```

Tracing docs also mention `npx @respan/cli setup` for coding-agent setup.

---

## MCP

**Status:** ✅ Docs advertise an MCP server for AI clients

| Detail | Value |
|---|---|
| **MCP** | `https://respan.ai/_mcp/server` (published on current docs pages) |
| **Compatible Clients** | Claude Code, Cursor, other MCP clients per docs |

---

## What It Does

Respan (formerly Keywords AI) is an **LLM engineering platform**: one gateway to **1,000+ models**, plus tracing, metrics, evals, prompt management, and agent security testing on a shared span model. Homepage H1: *"Route, observe, and evaluate every LLM call."* Docs: *"the full-stack AI engineering platform for LLM and agent products."*

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage closer: *"Built for AI agents. Break less. Ship more."* Docs overview: platform for *"LLM and agent products"*; tracing page covers OpenAI Agents SDK workflows |
| **Agent-specific primitive** | Agent workflow traces (LLM / tool / retrieval / agent-turn spans); `OpenAIAgentsInstrumentor`; per-customer identifiers and thread IDs |
| **Autonomy-compatible control plane** | Automatic **fallback**, caching, and spend limits without human failover |
| **M2M integration surface** | OpenAI-compatible **REST** at `https://api.respan.ai/api`, SDKs, MCP, `npx @respan/cli setup` |
| **Identity / delegation** | API keys; `customer_identifier` / `thread_identifier` metadata on spans |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unified chat endpoint** | Single URL for 1,000+ models |
| **Fallback chain** | Next model on error or rate limit |
| **Caching / spend limits** | Repeat-request cache; budgets per key, customer, or org |
| **Trace instrumentor** | Agent-run spans via `OpenAIAgentsInstrumentor` |
| **Evals** | LLM judge, code check, or human review on spans |

---

## Autonomy Model

```
Agent SDK → base URL https://api.respan.ai/api with Respan API key
    ↓
Gateway applies routing, limits, fallbacks, cache
    ↓
Provider response returned; traces recorded if instrumentor attached
```

---

## Identity and Delegation Model

- **API keys** scope org access.
- **Per-end-user metadata** (`customer_identifier`) supports multi-tenant agent apps.
- Rotate keys if an agent leaks credentials.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://api.respan.ai/api/chat/completions` |
| OpenAI SDK | Drop-in `base_url="https://api.respan.ai/api"` |
| Agents SDK | `OpenAIAgentsInstrumentor` — [docs](https://www.respan.ai/docs/integrations/openai-agents-sdk) |
| MCP | `https://respan.ai/_mcp/server` |

---

## Human-in-the-Loop Support

Dashboard for prompts, logs, evals, and limits; runtime is automated. Evaluators may include a human reviewer.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Call OpenAI directly** | No **central fallback**, **multi-model** routing, or **agent trace instrumentor** |
| **LiteLLM (see catalog entry)** | Respan is a **hosted** product with dashboard governance; LiteLLM is **self-hosted OSS** with overlapping gateway features |

---

## Use Cases

- **Multi-agent SaaS** — One gateway for all tenants
- **Reliability** — Fallback when a provider degrades
- **Cost visibility** — Trace-linked usage for agent debugging
