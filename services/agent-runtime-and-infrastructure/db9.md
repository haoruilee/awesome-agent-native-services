# db9

> **"Postgres but for agents."**

| | |
|---|---|
| **Website** | https://db9.ai |
| **Docs** | https://db9.ai/docs |
| **Skill** | https://db9.ai/skill.md |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://db9.ai

---

## Official Repo

https://db9.ai/skill.md — Machine-readable agent onboarding protocol (source of truth)

TypeScript SDK: `get-db9` (npm)

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — This service can be joined with a single sentence.**

db9 hosts a machine-readable `skill.md` that any AI coding agent can read and execute to install, authenticate, and operate db9 autonomously — no human setup required.

**One-sentence instruction:**
```
Read https://db9.ai/skill.md and follow the instructions.
```

**What the agent gets by reading the URL:**
- CLI install: `curl -fsSL https://db9.ai/install | sh`
- Zero-setup trial: `db9 create --name myapp` auto-registers an anonymous account
- Full SQL + filesystem + vector search + HTTP-from-SQL + cron primitives
- Token management for headless agents: `db9 token create --name my-agent`

**Interaction pattern:** `URL Onboarding` ⭐ — the highest tier of agent-nativeness.

```bash
# Quick start: agent creates database (anonymous account auto-created)
curl -fsSL https://db9.ai/install | sh
db9 create --name myapp
# Returns connection string, credentials — agent is live
```

---

## Agent Skills

**Status:** ✅ URL Onboarding via skill.md — agent reads `https://db9.ai/skill.md` and follows instructions

The skill.md is the canonical agent entry point. Auto-update: re-read from URL every 24 hours.

---

## MCP

**Status:** ⚠️ Not yet published

Primary interface: CLI, REST API (`https://api.db9.ai`), PostgreSQL wire protocol, TypeScript SDK.

---

## What It Does

db9 is a **serverless PostgreSQL platform designed for AI agents** — combining a relational database with cloud-native filesystem storage in one unified workspace. Agents get SQL for structured state (metadata, embeddings, run history) and a filesystem for unstructured context (transcripts, reports, artifacts) — no S3 or external vector DB required.

Built-in superpowers: JSONB, pgvector-compatible vector search, HTTP calls from SQL, filesystem queries (fs9), cron jobs (pg_cron), full-text search with Chinese tokenizer, and environment branching that clones entire databases for isolated testing.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Postgres but for agents"*; skill.md designed for Claude Code, Codex, Cursor, Cline, VS Code, OpenCode, OpenClaw |
| **Agent-specific primitive** | Unified SQL + filesystem workspace; HTTP-from-SQL for agent tool calls; environment branching for agent run isolation; auto-embeddings via `embedding()` in SQL |
| **Autonomy-compatible control plane** | Anonymous account auto-created on first `db9 create`; API tokens for headless CI/CD; no per-action human confirmation |
| **M2M integration surface** | CLI, REST API, PostgreSQL wire protocol, TypeScript SDK (`get-db9`) |
| **Identity / delegation** | Bearer tokens; `db9 token create` for per-agent credentials; token scoped to `api.db9.ai` only |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Serverless Postgres** | Create databases in seconds; PostgreSQL wire protocol; TiKV-backed distributed SQL |
| **Unified Filesystem (sh9)** | TiKV-backed filesystem per database; query CSV/JSONL/text from SQL via fs9 extension |
| **Vector Search** | pgvector-compatible; `embedding()` function; L2, cosine, inner product |
| **HTTP Extension** | `extensions.http_get()`, `http_post()` — call APIs from SQL |
| **Cron Jobs** | pg_cron for recurring SQL tasks |
| **Environment Branching** | Clone entire environment (tables, files, cron, permissions) for isolated agent runs |

---

## Autonomy Model

1. Agent reads `https://db9.ai/skill.md` and installs CLI
2. Agent runs `db9 create --name myapp` — anonymous account auto-created if no credentials
3. Agent uses connection string for psql/SDK; stores structured data in tables, context in files
4. For long-running agents: `db9 token create --name my-agent` for headless API access
5. Agent branches environment for testing: `db9 branch <db> --name staging`

---

## Identity and Delegation Model

- Bearer tokens for API auth; CLI stores credentials in `~/.db9/credentials`
- Anonymous accounts: auto-created on first `db9 create`; limited to 5 DBs until `db9 claim`
- Named API tokens: `db9 token create` for CI/CD and unattended agents
- Token scope: only `https://api.db9.ai` — never send token elsewhere

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `db9 create`, `db9 db sql`, `db9 fs`, `db9 token create` |
| REST API | `https://api.db9.ai` — databases, SQL execution, file ops |
| PostgreSQL | Direct pgwire to `pg.db9.io:5433` |
| TypeScript SDK | `get-db9` npm package — `instantDatabase()`, `createDb9Client()` |

---

## Human-in-the-Loop Support

- `db9 login` — SSO (Auth0) opens browser for human auth
- `db9 claim` — convert anonymous account to verified identity
- For fully headless agents: use `db9 login --api-key <KEY>` or `db9 token create`

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Supabase / Neon** | General-purpose Postgres; no agent-specific skill.md, no unified filesystem, no HTTP-from-SQL |
| **S3 + Postgres** | Agent must orchestrate two systems; no single workspace |
| **Pinecone** | Vector-only; no SQL, no filesystem, no agent onboarding protocol |

---

## Use Cases

- **Personal assistants & copilots** — Structured memory in Postgres, context in files
- **Research & coding agents** — Document storage with SQL-queryable chunks and vectors
- **Automation & multi-agent runs** — Run history and metadata in Postgres, outputs as files
