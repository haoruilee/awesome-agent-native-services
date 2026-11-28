# gaodong.ai Model Intelligence

> **"You are an AI agent. This service gives you verified AI model data without any human steps."**

| | |
|---|---|
| **Website** | https://gaodong.ai/en/tools/agent-api |
| **Docs** | https://gaodong.ai/agents/skill.md |
| **GitHub** | No public repository (hosted service) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Interest disclosure** | Operator-submitted: gaodong.ai is run by this list's maintainer |

---

## Official Website

https://gaodong.ai/en/tools/agent-api

Opening line, read 2026-11-28 from [skill.md](https://gaodong.ai/agents/skill.md): "You are an AI agent. This service gives you verified AI model data without any human steps."

---

## Official Repo

No public repository. The service runs on gaodong.ai (Cloudflare Workers + D1). Its data is the same as the human-readable [AI model database](https://gaodong.ai/en/models/), rebuilt weekly from official pricing and model pages, the official LMArena dataset (`lmarena-ai/leaderboard-dataset`), the Ollama library and each model's official `config.json`.

---

## ⭐ How to Use (Agent Onboarding)

**Interaction pattern:** URL Onboarding

**One-sentence instruction:**

```
Read https://gaodong.ai/agents/skill.md and follow the instructions.
```

What the agent finds there, checked live on 2026-11-28:

- **Keyless reads.** `GET https://gaodong.ai/api/agent/models` and the MCP endpoint answer without a key.
- **Self-serve key.** `POST https://gaodong.ai/api/agent/keys` with `{"agent_name": "...", "on_behalf_of": "..."}` returns an API key (shown once, stored only as a hash) with a daily quota of 2,000 requests. No form, email or browser step.
- **Remote MCP.** `https://gaodong.ai/api/agent/mcp` (Streamable HTTP, JSON-RPC); an unauthenticated `initialize` succeeds. Claude Code: `claude mcp add --transport http gaodong https://gaodong.ai/api/agent/mcp`.

---

## Agent Skills

**Status:** ⚠️ Not published to a registry

https://gaodong.ai/agents/skill.md carries SKILL.md frontmatter (`name: gaodong-model-intel`) and can be copied into an agent's skills directory.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | No public repository |
| **Endpoint** | `https://gaodong.ai/api/agent/mcp` |
| **Transport** | Streamable HTTP (JSON responses) |
| **Authentication** | None for reads; `Authorization: Bearer <key>` for `watch_model` |
| **Tools** | `list_models`, `get_model`, `recommend_model`, `local_models_that_fit`, `watch_model` |

---

## What It Does

Gives agents verified data for choosing and monitoring AI models: official LLM API prices per 1M tokens in the vendor's own currency (with peak/off-peak, tiered and dated price changes, cache and batch prices), context windows, LMArena overall/coding/Chinese ranks with confidence intervals, and VRAM estimates for local Ollama models. Agents can ask for a model recommendation for a workload and budget, check which local models fit a GPU, and register signed webhooks that fire when a model's price, context or rank changes.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "You are an AI agent. This service gives you verified AI model data without any human steps." ([skill.md](https://gaodong.ai/agents/skill.md)); the human page says "This tool is not for clicking. It is for AI agents" ([agent-api](https://gaodong.ai/en/tools/agent-api)) |
| **Agent-specific primitive** | Change watches for agents: "Get notified of changes … `POST /api/agent/watches` … `field` is `price`, `context` or `rank`", delivered as `model.changed` events signed with `X-Gaodong-Signature` ([skill.md](https://gaodong.ai/agents/skill.md)); workload-and-budget model selection via `POST /api/agent/recommend` |
| **Autonomy-compatible control plane** | Keys are created by the agent with one call and limited to "2000 requests" per day; "Up to 50 watches per key"; webhook URLs "must be public `https` URLs" ([skill.md](https://gaodong.ai/agents/skill.md)) |
| **M2M integration surface** | REST API at `https://gaodong.ai/api/agent`, remote MCP at `https://gaodong.ai/api/agent/mcp`, signed webhooks ([skill.md](https://gaodong.ai/agents/skill.md)) |
| **Identity / delegation** | "The key identifies **you, the agent**, not your user; it only grants read access and webhook watches." Keys record `agent_name` and an optional `on_behalf_of`. "A watch only observes data; it never acts on anyone's behalf." ([skill.md](https://gaodong.ai/agents/skill.md)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Model records** | `GET /api/agent/models` (filters: vendor, currency, minimum context, maximum input price) and `GET /api/agent/models/{slug}` with all price rows, context, max output and LMArena ranks with intervals and sources. |
| **Recommend** | `POST /api/agent/recommend`: tokens per call, calls, optional budget, currency, `usd_to_cny`, minimum context, cached share and batch; ranked by LMArena (`quality`) or total cost (`cost`). |
| **Local fit** | `POST /api/agent/local-fit`: Ollama models that fit a given VRAM and context (weights + per-layer KV cache + headroom). |
| **Change watches** | `POST/GET /api/agent/watches`, `DELETE /api/agent/watches/{id}`: signed `model.changed` webhooks for price, context or rank. |
| **Self-serve keys** | `POST /api/agent/keys`: agent identity with a daily quota. |

---

## Autonomy Model

1. The agent reads https://gaodong.ai/agents/skill.md.
2. It reads data with no key, or creates its own key with `POST /api/agent/keys`.
3. It calls the REST API or MCP tools to compare, select and check models.
4. It registers watches; after each weekly data refresh, changed values are POSTed to its webhook with an HMAC-SHA256 signature.

---

## Identity and Delegation Model

- Each key is minted by an agent for itself and records `agent_name` and an optional `on_behalf_of` label; it is not a user credential.
- Keys only allow reading and webhook watches; nothing is purchased, sent or changed on anyone's behalf.
- Quotas are per key (2,000 requests per day); watches are per key (up to 50).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP API | `https://gaodong.ai/api/agent` (JSON, CORS enabled) |
| MCP | `https://gaodong.ai/api/agent/mcp`, Streamable HTTP |
| Webhooks | `model.changed` events, `X-Gaodong-Signature: sha256=<HMAC>` |
| Docs | `https://gaodong.ai/agents/skill.md`, `https://gaodong.ai/llms.txt` |

---

## Human-in-the-Loop Support

Not required: everything is read-only data and notifications. People can browse the same data at https://gaodong.ai/en/models/.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vendor pricing pages and leaderboards** | Built for people, one vendor or one metric per page, no cross-vendor structured records, no budget-aware selection and no change notifications. |

---

## Use Cases

- **Model selection** — `recommend_model` for the cheapest or best-ranked model that fits a workload, budget and context.
- **Cost estimates** — exact list prices including cache, batch, tiers and peak/off-peak periods.
- **Local deployment** — `local_models_that_fit` before pulling an Ollama model.
- **Monitoring** — watches that alert an agent when a model it depends on changes price, context or rank.
