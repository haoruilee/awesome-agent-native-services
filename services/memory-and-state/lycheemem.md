# LycheeMem

> **"LycheeMem is a compact memory framework for LLM agents."**

| | |
|---|---|
| **Website** | https://lycheemem.github.io/ |
| **Docs** | https://github.com/LycheeMem/LycheeMem/blob/master/README.md |
| **GitHub** | https://github.com/LycheeMem/LycheeMem |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social)](https://github.com/LycheeMem/LycheeMem) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://lycheemem.github.io/

---

## Official Repo

https://github.com/LycheeMem/LycheeMem — Server, LangGraph memory pipeline, OpenClaw plugin, HTTP MCP

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + `MCP (HTTP)` + optional OpenClaw plugin

```bash
git clone https://github.com/LycheeMem/LycheeMem.git && cd LycheeMem
pip install -e ".[dev]"
cp .env.example .env   # set LLM_MODEL, LLM_API_KEY, embedder vars
python main.py         # API at http://localhost:8000 — docs at /docs
```

**MCP (remote HTTP):** After the server is running, point MCP clients at `http://localhost:8000/mcp` — use `POST /mcp` for JSON-RPC; reuse `Mcp-Session-Id` from `initialize` on later requests (see the MCP section in the repo README).

**First API calls:** `POST /memory/search` → `POST /memory/synthesize` → `POST /memory/reason` with a `session_id` (see README API Reference).

**OpenClaw:** `openclaw plugins install "/path/to/LycheeMem/openclaw-plugin"` then `openclaw gateway restart` — see [INSTALL_OPENCLAW.md](https://github.com/LycheeMem/LycheeMem/blob/master/openclaw-plugin/INSTALL_OPENCLAW.md).

---

## Agent Skills

**Status:** ⚠️ No single global `SKILL.md` install via `npx skills add` — OpenClaw plugin ships with the repo; see [openclaw-plugin/](https://github.com/LycheeMem/LycheeMem/tree/master/openclaw-plugin).

```bash
npx clawhub@latest search lycheemem memory
```

---

## MCP

**Status:** ✅ Available (HTTP endpoint on the self-hosted server)

| Detail | Value |
|---|---|
| **Endpoint** | `http://localhost:8000/mcp` (when `python main.py` is running) |
| **Transport** | Streamable HTTP — `POST /mcp` (JSON-RPC); `GET /mcp` for SSE where supported |
| **Session** | Server returns `Mcp-Session-Id` during `initialize`; reuse on subsequent requests |
| **Compatible Clients** | Any MCP client that supports remote HTTP servers (configure URL per client docs) |

Example Cursor-style config (local server):

```json
{
  "mcpServers": {
    "lycheemem": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

---

## What It Does

LycheeMem is a self-hosted memory stack for LLM agents built around a fixed LangGraph pipeline: working memory with **dual-threshold token budgets** (warn at 70%, block at 90% with compression), **semantic memory** backed by SQLite + LanceDB with typed `MemoryRecord`s, record fusion, and action-aware retrieval, plus **procedural memory** (skill store) with HyDE-style retrieval. A background consolidator runs after turns to compact conversations, extract skills, and persist structured records — without blocking the user-facing response path.

Agents integrate through REST, HTTP MCP, or the OpenClaw plugin (`lychee_memory_smart_search`, hooks for automatic turn mirroring, consolidation on session boundaries).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"LycheeMem is a compact memory framework for LLM agents"* and *"gradually extends toward action-aware, usage-aware memory for more capable agentic systems"* — [source](https://github.com/LycheeMem/LycheeMem/blob/master/README.md) |
| **Agent-specific primitive** | **Three-store agent memory pipeline** (working / semantic / procedural) with LLM-as-judge synthesis, typed semantic records, skill extraction from tool traces, and token-budget-governed compression — not a generic document store |
| **Autonomy-compatible control plane** | Agents call search → synthesize → reason and trigger `POST /memory/consolidate/{session_id}`; consolidator runs in the background; no human must approve each memory write |
| **M2M integration surface** | REST API (`/docs`), HTTP `/mcp`, OpenClaw plugin, Python package (`pip install -e .`) |
| **Identity / delegation** | **`session_id`** namespaces conversation and consolidation; API responses include **provenance** linking fused context to source records; optional HTTP basic auth for multi-user setups in demos |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Working memory** | Session turns and summaries under dual token thresholds with async pre-compression |
| **Semantic memory** | Typed `MemoryRecord`s, compact semantic engine, SQLite + LanceDB, record fusion, action-aware search planning |
| **Procedural memory** | Skill entries with HyDE retrieval |
| **REST: `/memory/search`** | Unified retrieval over semantic channel + skill store |
| **REST: `/memory/synthesize`** | LLM-as-judge fusion into `background_context` + `skill_reuse_plan` |
| **REST: `/memory/reason`** | Grounded generation with optional `append_to_session` |
| **REST: `/memory/consolidate/{session_id}`** | Manual or automatic post-turn consolidation |
| **HTTP MCP** | Tool surface for MCP clients against the running server |
| **OpenClaw plugin** | Hooks + `lychee_memory_smart_search` / `lychee_memory_consolidate` |

---

## Autonomy Model

```
Agent (or host) starts LycheeMem: python main.py
    ↓
Agent uses MCP tools or REST: search → synthesize → reason with session_id
    ↓
Background ConsolidatorAgent merges new turns into semantic + skill stores (novelty-gated)
    ↓
Next turn: agent retrieves fused context + provenance without human curation
```

---

## Identity and Delegation Model

- **Session isolation** — `session_id` ties working history, consolidation, and reasoning calls together.
- **Attribution in context** — `provenance` arrays in search/synthesize responses tie generated context back to semantic-memory sources.
- **Multi-user boundary** — Optional credentials in example scripts; production deployments should enforce auth at the reverse proxy or API gateway.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | FastAPI on port 8000 — `/memory/*`, OpenAPI at `/docs` |
| HTTP MCP | `POST /mcp`, `GET /mcp` (SSE), `Mcp-Session-Id` header |
| Python | `pip install -e ".[dev]"` from cloned repo |
| OpenClaw | Local plugin path install |

---

## Human-in-the-Loop Support

Humans may use the optional `web-demo` chat UI or OpenAPI `/docs` for debugging; the agent operational path is fully API- and MCP-driven. No built-in approval gate for memory writes — operators enforce policy at deployment (network ACLs, auth, rate limits).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vector DB + chunk RAG** | No agent-oriented working-memory compression thresholds, typed semantic action records, procedural skill store, or LangGraph consolidation pipeline |
| **Human note apps (Notion, Obsidian API)** | Human-first UX; no multi-stage agent memory fusion, tool-trace skill extraction, or MCP tool surface aligned to agent sessions |

---

## Use Cases

- **Long-horizon coding agents** — Accumulate project facts and successful tool patterns across sessions via OpenClaw or MCP
- **Research assistants** — Session-scoped reasoning with retrievable semantic graph + provenance for grounded answers
- **Self-hosted agent memory** — Full control over data residency (SQLite + LanceDB on your hardware)
