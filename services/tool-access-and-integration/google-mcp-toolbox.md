# MCP Toolbox for Databases

> **"MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your enterprise databases."**

| | |
|---|---|
| **Website** | https://mcp-toolbox.dev/ |
| **Docs** | https://mcp-toolbox.dev/ |
| **GitHub** | https://github.com/googleapis/mcp-toolbox |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social)](https://github.com/googleapis/mcp-toolbox) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://mcp-toolbox.dev/

---

## Official Repo

https://github.com/googleapis/mcp-toolbox

---

## How to Use (Agent Onboarding)

**Prebuilt MCP tools (npm)** — add to MCP config (example from README for Postgres):

```json
{
  "mcpServers": {
    "toolbox-postgres": {
      "command": "npx",
      "args": ["-y", "@toolbox-sdk/server", "--prebuilt=postgres"]
    }
  }
}
```

Set **connection environment variables** per [Prebuilt Tools Reference](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/).

**SDKs** — Python (`toolbox-core`), JS (`@toolbox-sdk/core`), Go, Java — see badges and docs on [GitHub README](https://github.com/googleapis/mcp-toolbox).

**Custom tools framework** — define restricted, structured, or NL2SQL-style tools for production agents — [documentation](https://mcp-toolbox.dev/).

---

## Agent Skills

**Status:** ⚠️ Not yet published as a dedicated `npx skills add …` pack

Search community skills: `npx clawhub@latest search mcp-toolbox`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ MCP server (`@toolbox-sdk/server`) + prebuilt database packs

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/googleapis/mcp-toolbox |
| **Transport** | stdio via `npx` (typical) |
| **Compatible Clients** | Gemini CLI, Google Antigravity, Claude Code, Codex, other MCP IDEs — per README |

---

## What It Does

MCP Toolbox exposes **database operations as MCP tools** in two modes: **prebuilt generic tools** (schema discovery, SQL execution, etc.) for fast IDE/agent connectivity, and a **custom tools framework** for production agents with **auth (including IAM)**, **restricted access**, **structured queries**, **semantic search**, **connection pooling**, and **OpenTelemetry** observability.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"connects your **AI agents**, IDEs, and applications directly to your **enterprise databases**"* and quick start names **Gemini CLI, Antigravity, Claude Code, Codex** — [GitHub README](https://github.com/googleapis/mcp-toolbox) |
| **Agent-specific primitive** | **MCP tool surface for data + schema with safety rails** (prebuilt + custom tool definitions, restricted access patterns) — not merely exposing raw SQL to humans |
| **Autonomy-compatible control plane** | After env/IAM configuration, agents call MCP tools without per-query dashboard clicks (subject to configured policies) |
| **M2M integration surface** | MCP server, multi-language SDKs, OTEL — see docs |
| **Identity / delegation** | **Integrated authentication / IAM** and tool-level access patterns documented as first-class — agents operate under configured service or user delegation, with audit via standard DB and OTEL pipelines |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Prebuilt tools** | e.g. `list_tables`, `execute_sql` (exact set per database pack) |
| **Prebuilt packs** | AlloyDB, BigQuery, Cloud SQL (Postgres/MySQL/SQL Server), Spanner, Firestore, Knowledge Catalog, etc. — [README](https://github.com/googleapis/mcp-toolbox) |
| **Custom tools** | Structured queries, semantic search, NL2SQL with safety controls |
| **Auth** | IAM and integrated auth flows per documentation |
| **Observability** | OpenTelemetry metrics and tracing |

---

## Autonomy Model

```
Admin configures DB credentials / IAM + MCP Toolbox server
  ↓
Agent host starts MCP server (npx @toolbox-sdk/server …)
  ↓
Agent calls toolbox tools (schema introspection, governed SQL, …)
  ↓
Toolbox enforces configured restrictions; results return to the agent
```

---

## Identity and Delegation Model

- **Database credentials** via environment variables or cloud IAM bindings per prebuilt config docs.
- **Tool-level restrictions** — custom framework emphasizes controlled access for production agents.
- **Observability** — OTEL for tracing tool/database usage in enterprise pipelines.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | `@toolbox-sdk/server` via npx |
| **SDKs** | Python, JS/TS, Go, Java |
| **Docs** | https://mcp-toolbox.dev/ |

---

## Human-in-the-Loop Support

Initial database policy design, IAM roles, and connection secrets are operator responsibilities. Agents consume tools within those guardrails.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Ad-hoc SQL over chat** | No **MCP tool contract**, no bundled **auth/IAM + pooling + OTEL** story |
| **ORM read-only APIs** | Not shaped as **agent-discoverable tools** with prebuilt schema helpers |
| **Human BI tools** | Not M2M-first for autonomous agent loops |

---

## Use Cases

- **Schema-aware coding agents** — generate migrations and queries with live metadata
- **Data exploration in IDE** — Claude/Cursor/Gemini CLI inspect tables safely
- **Production agents** — custom tools with restricted SQL and semantic retrieval
