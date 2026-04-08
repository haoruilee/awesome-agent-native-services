# OpenRouter

> **"The Unified Interface For LLMs."**

| | |
|---|---|
| **Website** | https://openrouter.ai |
| **Docs** | https://openrouter.ai/docs/quickstart |
| **GitHub** | https://github.com/OpenRouterTeam |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://openrouter.ai

---

## Official Repo

OpenRouter publishes SDKs and examples across the **OpenRouterTeam** GitHub organization — https://github.com/OpenRouterTeam

---

## How to Use (Agent Onboarding)

**OpenAI-compatible REST — one API key for 300+ models across many providers.**

```bash
# Docs: https://openrouter.ai/docs/quickstart
export OPENROUTER_API_KEY=...
# Use OpenAI SDK with base_url https://openrouter.ai/api/v1
```

Official SDKs: TypeScript, Python, Go, Java — see [SDK](https://openrouter.ai/sdk).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills catalog entry found.

```bash
npx clawhub@latest search openrouter
```

---

## MCP

**Status:** ⚠️ No first-party OpenRouter MCP server documented as core product; integration is primarily **HTTP / SDK**.

---

## What It Does

OpenRouter provides a **single OpenAI-compatible API** to access **hundreds of models** from dozens of labs with **routing**, **uptime optimization**, **pricing transparency**, and **usage analytics**. It is widely used for **agentic and multi-model workflows** (tool calling, fallbacks, provider selection) without maintaining separate billing and client integrations per provider — see homepage *"Featured Agents"* and [provider selection](https://openrouter.ai/docs/guides/routing/provider-selection) docs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage highlights **agent apps** and **multi-model** production patterns; docs cover **tool calling** and **routing** for autonomous workloads |
| **Agent-specific primitive** | **Cross-provider routing with automatic failover**; **model / app rankings**; **data policies** controlling which providers receive prompts — primitives tuned to **untrusted agent** output distribution |
| **Autonomy-compatible control plane** | Agents call one endpoint continuously; credits and keys are **programmatic**; no per-request human approval |
| **M2M integration surface** | REST (OpenAI-compatible), official multi-language SDKs |
| **Identity / delegation** | **Org accounts**, **API keys**, **usage attribution** per key/app; **privacy / logging policies** per org |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unified chat API** | OpenAI-compatible `/chat/completions` across many models |
| **Model routing** | Provider selection, sorting by price/latency, uptime features |
| **Credits & billing** | Single balance for any model on the platform |
| **App rankings & analytics** | Visibility into model usage across public apps |
| **Data policies** | Control logging and provider eligibility |

---

## Autonomy Model

```
Agent uses OpenAI SDK pointed at OpenRouter base URL
    ↓
Request includes model slug (e.g. anthropic/claude-…) and optional routing hints
    ↓
OpenRouter selects provider / handles failover
    ↓
Tool calls and multi-turn loops proceed like native OpenAI — one key, many backends
```

---

## Identity and Delegation Model

- **API keys** belong to users or orgs; usage billed to the owning account.
- **Data policy** settings govern what OpenRouter may log or which providers may process prompts.
- **Public app listings** (optional) tie usage to named applications for transparency.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://openrouter.ai/api/v1` — OpenAI-compatible |
| SDKs | TypeScript, Python, Go, Java — https://openrouter.ai/sdk |
| Dashboard | Account, credits, keys — secondary to API |

---

## Human-in-the-Loop Support

Not a HITL product; org admins may govern policies and spending outside the agent loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Single-vendor API** | Locks agent to one lab; OpenRouter spans providers with unified billing |
| **Self-managed router only** | You operate failover, pricing feeds, and provider contracts yourself |
| **Raw HTTP to each lab** | No cross-provider analytics, rankings, or centralized credit model |

---

## Use Cases

- **Multi-model agents** — cheap model for triage, frontier model for execution
- **Resilient production** — automatic provider failover without agent code changes
- **Global apps** — edge-routed inference with consistent SDK
