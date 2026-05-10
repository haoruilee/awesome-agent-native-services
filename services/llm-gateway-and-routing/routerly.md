# Routerly

> **"Self-hosted LLM gateway that routes requests across AI providers (OpenAI, Anthropic, Gemini, Mistral, Ollama) using intelligent multi-policy scoring — including an LLM-native routing policy. Drop-in compatible: just swap the base URL. No database required, built-in cost tracking, budget enforcement and multi-tenant isolation."**

| | |
|---|---|
| **Website** | https://github.com/Inebrio/Routerly |
| **Docs** | https://github.com/Inebrio/Routerly#readme |
| **GitHub** | https://github.com/Inebrio/Routerly |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing](README.md) |
| **License** | AGPL-3.0 · v0.1.5 (March 2026) |

---

## Official Website

https://github.com/Inebrio/Routerly

---

## Official Repo

https://github.com/Inebrio/Routerly

---

## How to Use (Agent Onboarding)

```
# Run the gateway:
docker run -p 8080:8080 -v ./routerly.json:/config/routerly.json inebrio/routerly:latest

# Point any OpenAI-compatible client at it:
export OPENAI_BASE_URL=http://localhost:8080/v1
export OPENAI_API_KEY=<your tenant key>
```

No Redis, no Postgres — config is a single JSON file.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

```bash
npx clawhub@latest search routerly
```

---

## MCP

**Status:** ⚠️ Not yet published. Routerly fronts LLM endpoints; an MCP-on-MCP routing surface is on the roadmap.

| Detail | Value |
|---|---|
| **Transport** | OpenAI / Anthropic-compatible HTTP |
| **Compatible Clients** | OpenAI SDK, Anthropic SDK, any agent runtime |

---

## What It Does

Routerly is a **self-hosted LLM gateway** with one distinguishing primitive: an **LLM-native routing policy** that uses a small LLM to make per-request routing decisions, alongside conventional rule-based policies (cost, latency, fallback, sticky session). The other policies are familiar — budgets, tenant isolation, cost tracking — but the operational story is unusual: **no database, no Redis**, just a JSON config file. That makes it interesting for small teams running a single agent fleet who want intelligent routing without operating a stateful gateway cluster.

It is drop-in compatible with the OpenAI and Anthropic SDKs (just swap the base URL), and supports OpenAI, Anthropic, Gemini, Mistral, and local Ollama.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo description frames the gateway around per-tenant agent traffic with budget enforcement and intelligent routing |
| **Agent-specific primitive** | LLM-native routing policy (small LLM picks the destination model per request); per-tenant budget enforcement that fails closed |
| **Autonomy-compatible control plane** | Drop-in URL swap; no per-call human approval; budgets are enforced automatically |
| **M2M integration surface** | OpenAI- and Anthropic-compatible HTTP; JSON config |
| **Identity / delegation** | Multi-tenant isolation; per-tenant API keys; per-tenant cost ledger |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **LLM-native Routing Policy** | A small LLM scores candidates and picks per request |
| **Multi-Policy Scoring** | Cost / latency / availability / sticky-session policies compose |
| **Drop-in Base URL** | OpenAI + Anthropic SDK compatibility — swap base URL only |
| **Budget Enforcement** | Per-tenant caps that fail closed at the gateway |
| **Multi-Tenant Isolation** | Per-tenant keys, ledgers, and policies |
| **Zero-Dependency Operation** | No DB, no Redis — single binary + JSON |

---

## Autonomy Model

1. Operator writes a `routerly.json` declaring providers, tenants, budgets, and policies.
2. Operator runs the gateway (Docker single binary).
3. Agent points its OpenAI / Anthropic client at the gateway URL with a tenant key.
4. Gateway scores candidates (including the LLM-native policy if enabled) and forwards.
5. Cost is tallied; budget breaches fail closed.

---

## Identity and Delegation Model

- Per-tenant API keys (the agent's tenant identity at the gateway).
- Per-tenant budgets and ledgers.
- Audit log of every routed request, including which provider was chosen and why.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP | `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` |
| Anthropic-compatible HTTP | `/v1/messages` |
| JSON Config | Single file — providers, tenants, policies, budgets |
| Docker / single binary | Self-host anywhere |

---

## Human-in-the-Loop Support

Out of scope for the gateway itself; budget breach events can be wired to Slack / email or to HumanLayer / Inferable for "approve overage" flows.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **LiteLLM proxy** | Excellent open-source gateway (already in catalog) — Routerly differs by adding an LLM-native routing policy and operating with zero stateful dependencies |
| **Portkey / Helicone** | Hosted SaaS; Routerly's pitch is "no DB, no Redis, just a JSON config" |
| **Plain reverse proxy** | No budget enforcement, no per-tenant isolation, no policy scoring |

---

## Use Cases

- **Tiny ops budget** — small teams that want intelligent routing without running Redis / Postgres
- **Per-tenant agent SaaS** — issue tenant keys; gateway enforces budgets and isolates ledgers
- **Cost-aware fleets** — LLM-native policy weighs price vs. capability per request, so cheap requests don't burn frontier-model dollars
