# Helicone

> **"Build Reliable AI Apps"** — AI Gateway & LLM observability.

| | |
|---|---|
| **Website** | https://www.helicone.ai |
| **Docs** | https://docs.helicone.ai |
| **GitHub** | N/A (primary product is hosted gateway + dashboard) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://www.helicone.ai

---

## Official Repo

Helicone is primarily a **hosted platform**. Integrate via **OpenAI-compatible gateway** and dashboard — see [Quickstart](https://docs.helicone.ai/).

---

## How to Use (Agent Onboarding)

**OpenAI-compatible AI Gateway — point the OpenAI SDK at Helicone.**

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://ai-gateway.helicone.ai",
  apiKey: process.env.HELICONE_API_KEY,
});
```

Python and cURL examples: same base URL — see [Quickstart](https://docs.helicone.ai/).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills repo listed.

```bash
npx clawhub@latest search helicone
```

---

## MCP

**Status:** ⚠️ No dedicated Helicone MCP server documented as primary surface.

---

## What It Does

Helicone provides an **OpenAI-compatible AI Gateway** to **100+ models** (OpenAI, Anthropic, Google, Groq, etc.) with **unified billing / credits**, **automatic fallbacks**, and **full request logging** in the Helicone dashboard. Agents and apps use a **single API key** instead of juggling many provider keys — optional **bring-your-own-key** mode for advanced control — see [Quickstart](https://docs.helicone.ai/).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Positioned for **AI applications** and **LLM production**; gateway + observability for high-volume **programmatic** callers |
| **Agent-specific primitive** | **Unified multi-model gateway** with **0% markup credits**, **automatic provider fallback**, and **per-request tracing** — designed for autonomous loops that cannot pause for human key rotation |
| **Autonomy-compatible control plane** | Agents call the gateway continuously; failures trigger **configured fallbacks** without operator intervention |
| **M2M integration surface** | OpenAI-compatible **REST**; works with OpenAI SDK in TS/Python |
| **Identity / delegation** | **Helicone API keys**; org-level **API keys** page; requests attributed in **Requests** tab |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AI Gateway** | `https://ai-gateway.helicone.ai` — OpenAI-compatible |
| **Unified credits** | One balance across many underlying providers (hosted keys) |
| **Fallbacks** | Automatic routing when a provider is degraded |
| **Observability** | Logs, metrics, and dashboards per request |
| **BYOK** | Optional use of your own provider keys |

---

## Autonomy Model

```
Agent uses OpenAI SDK with Helicone base URL + Helicone API key
    ↓
Helicone routes to selected model / provider
    ↓
On provider outage → automatic fallback (per docs)
    ↓
Every call logged for debugging and cost tracking
```

---

## Identity and Delegation Model

- **Helicone accounts** own API keys and credit balance.
- **Requests** are attributed to keys and projects in the dashboard.
- **BYOK** mode delegates provider billing to the customer while Helicone remains the integration edge.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | OpenAI-compatible `chat/completions` at `ai-gateway.helicone.ai` |
| Dashboard | https://us.helicone.ai — keys, requests, providers |
| Docs | https://docs.helicone.ai |

---

## Human-in-the-Loop Support

Teams review traces and metrics in the UI; the hot path is unattended.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Direct OpenAI only** | No built-in multi-provider routing or unified credit pool |
| **Raw log shipping** | No drop-in OpenAI base URL swap for 100+ models |
| **Self-hosted LiteLLM** | You operate infra; Helicone is hosted gateway + dashboard |

---

## Use Cases

- **Fast agent prototyping** — one key, many models, immediate logs
- **Production reliability** — provider fallbacks without custom retry code
- **Cost visibility** — centralized request stream for finance and debugging
