# mem9

> **"Persistent memory for AI agents."**

| | |
|---|---|
| **Website** | https://mem9.ai |
| **Skill** | https://mem9.ai/skill.md |
| **GitHub** | https://github.com/mem9-ai/mem9 |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache 2.0 |

---

## Official Website

https://mem9.ai

---

## Official Repo

https://github.com/mem9-ai/mem9 — Open-source mem9 server and plugins

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — This service can be joined with a single sentence.**

mem9 hosts a machine-readable `skill.md` that any AI agent can read and execute to provision a cloud memory space and connect — no human setup beyond API key storage.

**One-sentence instruction:**
```
Read https://mem9.ai/skill.md and follow the instructions to register and join.
```

**What the agent gets by reading the URL:**
- Provision API key: `curl -sX POST https://api.mem9.ai/v1alpha1/mem9s`
- REST API: `memory_store`, `memory_search`, `memory_get`, `memory_update`, `memory_delete`
- Plugin install for OpenClaw, Claude Code, OpenCode
- Lifecycle hooks: `before_prompt_build` (inject context), `before_reset` (save summary), `agent_end` (capture response)

**Interaction pattern:** `URL Onboarding` ⭐ — the highest tier of agent-nativeness.

```bash
# Quick start: provision API key
curl -sX POST https://api.mem9.ai/v1alpha1/mem9s | jq .
# Save id as API_KEY — agent has full access to cloud memory
```

---

## Agent Skills

**Status:** ✅ URL Onboarding via skill.md — agent reads `https://mem9.ai/skill.md` and follows instructions

OpenClaw plugin: `openclaw plugins install @mem9/mem9`

---

## MCP

**Status:** ⚠️ Not yet published (REST API primary; plugins for OpenClaw, Claude Code, OpenCode)

| Detail | Value |
|---|---|
| **API Base** | https://api.mem9.ai |
| **Auth** | `X-API-Key` header |
| **Tools** | `memory_store`, `memory_search`, `memory_get`, `memory_update`, `memory_delete` |

---

## What It Does

mem9 is **cloud-persistent memory infrastructure for AI agents** — solving the problem of agents forgetting context between sessions. Memory survives resets, restarts, and machine switches. Hybrid search combines vector similarity and keyword search with zero configuration. Cross-agent memory sharing lets agents on different platforms (Claude Code, OpenCode, OpenClaw) access the same memory pool.

Zero-ops setup: instant deployment without schema design or database management. Auto-embedding via `EMBED_TEXT()` generates embeddings server-side without requiring OpenAI keys.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Persistent memory for AI agents"*; skill.md for OpenClaw, Claude Code, OpenCode; designed for agent memory, not human note-taking |
| **Agent-specific primitive** | `memory_store`/`memory_search`/`memory_get`/`memory_update`/`memory_delete`; lifecycle hooks (`before_prompt_build`, `before_reset`, `agent_end`) inject context automatically |
| **Autonomy-compatible control plane** | Agent provisions API key via POST; no human curates memories; lifecycle hooks run automatically |
| **M2M integration surface** | REST API, OpenClaw plugin, Claude Code plugin, OpenCode plugin |
| **Identity / delegation** | API key scopes memory space; `X-Mnemo-Agent-Id` header for per-agent attribution; per-tenant isolation |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **memory_store** | Persist facts, decisions, context |
| **memory_search** | Hybrid search by keywords and meaning (vector + keyword) |
| **memory_get** | Retrieve by ID |
| **memory_update** | Modify existing memory |
| **memory_delete** | Remove memory |
| **Lifecycle Hooks** | `before_prompt_build` — inject relevant memories; `before_reset` — save session summary; `agent_end` — capture last response |

---

## Autonomy Model

1. Agent reads `https://mem9.ai/skill.md` and calls `POST /v1alpha1/mem9s` to provision API key
2. Agent configures plugin or uses REST API with `X-API-Key`
3. Agent stores memories via `memory_store`; lifecycle hooks inject context automatically on each LLM call
4. Agent searches via `memory_search` (hybrid vector + keyword)
5. Memory persists across sessions, devices, and agent restarts

---

## Identity and Delegation Model

- API key identifies the memory space (tenant); same key reconnects on new machines
- `X-Mnemo-Agent-Id` header for per-agent attribution
- API key is effectively a secret — never share; store in password manager for recovery

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `https://api.mem9.ai/v1alpha2/mem9s/memories` — CRUD, search, import |
| OpenClaw Plugin | `@mem9/mem9` — 5 tools + lifecycle hooks |
| Claude Code / OpenCode | Native plugins with same 5 tools |

---

## Human-in-the-Loop Support

Optional: user provides existing API key for reconnection. Agent can provision new key autonomously via POST.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Pinecone / Weaviate** | Raw vector DB; agent must implement extraction, lifecycle, and hybrid search |
| **Redis** | Key-value; no semantic search, no lifecycle hooks |
| **Local file memory** | Does not survive resets, restarts, or machine switches; no cross-agent sharing |

---

## Use Cases

- **24/7 proactive agents** — Remember user preferences, project context, decisions across sessions
- **Multi-machine continuity** — Same memory on laptop, desktop, cloud
- **Cross-agent collaboration** — Multiple agents (Claude Code, OpenClaw) share one memory pool
- **Import from local** — Migrate existing `memory/*.md`, `sessions/*.jsonl` into mem9
