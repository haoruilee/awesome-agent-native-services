# Cognee

> **"Memory control plane for AI Agents in 6 lines of code."**

| | |
|---|---|
| **Website** | https://www.cognee.ai |
| **Docs** | https://docs.cognee.ai |
| **GitHub** | https://github.com/topoteretes/cognee |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Stars** | 17,000+ · #1 Trendshift GitHub Repository of the Day · ~5.3M SDK runs / 30 days |

---

## Official Website

https://www.cognee.ai

---

## Official Repo

https://github.com/topoteretes/cognee

---

## How to Use (Agent Onboarding)

```
pip install cognee
# then:
import cognee
await cognee.add(documents)
await cognee.cognify()        # build the world model
results = await cognee.search("...")
```

First-party integrations ship for Claude Code, Codex, Cursor, LangGraph, CrewAI, Continue, Hermes, OpenClaw, plus an MCP server.

---

## Agent Skills

**Status:** ⚠️ No `SKILL.md` published by Cognee directly, but Cognee is **listed as a runtime target** by other catalog entries' skills.

```bash
npx clawhub@latest search cognee
```

---

## MCP

**Status:** ✅ Available — first-party MCP server.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/topoteretes/cognee-mcp (sibling repo) |
| **Transport** | stdio / Streamable HTTP |
| **Compatible Clients** | Claude Code, Cursor, Codex, OpenClaw, any MCP-compatible runtime |

---

## What It Does

Cognee is a **memory control plane** that ingests an agent's data sources (warehouses, vector stores, files, APIs), automatically extracts ontologies, builds and maintains a **managed world model** (graph + vectors), and serves recall back to agents. The pitch is "model your agent's world" — instead of stuffing raw chunks into a context window, the agent reasons over a structured representation of what it knows.

Three operational stages:

1. **Ingest** — connect Snowflake, Postgres, Slack, PDFs, MD files, REST APIs.
2. **Reason** — Cognee builds the ontology + managed graph + recall tuning that compounds with use.
3. **Act** — agent calls `cognee.search(...)` from Claude Code, LangGraph, OpenClaw, MCP-compatible runtimes, etc.

The library is open-source; Cognee Cloud is the optional managed tier (free locally; pay only when scaling).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"The brain behind your agents"* / *"Memory control plane for AI Agents in 6 lines of code"* |
| **Agent-specific primitive** | Auto-extracted ontologies, managed world model that compounds with use, agent-permissioned recall |
| **Autonomy-compatible control plane** | Ingestion + cognification + recall are programmatic; agent does not curate the graph by hand |
| **M2M integration surface** | Python SDK + 28+ data-source connectors + MCP server + framework adapters |
| **Identity / delegation** | Fine-grained per-agent and per-tenant permissions on memory |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`cognee.add(...)`** | Ingest from any of 28+ sources (warehouses, vector stores, docs, APIs) |
| **`cognee.cognify()`** | Build the world model — auto-ontology + managed graph + embeddings |
| **`cognee.search(...)`** | Hybrid retrieval over the world model |
| **Custom Ontologies** | Override or extend the auto-extracted schema |
| **Permissions Control** | Per-agent / per-tenant access boundaries |
| **MCP Server** | Any MCP host can read/write cognee memory |

---

## Autonomy Model

1. Operator points Cognee at data sources via adapters.
2. Agent calls `cognee.add(...)` whenever new content arrives.
3. `cognee.cognify()` runs (manually or on a schedule) to update the world model.
4. Agent calls `cognee.search(query)` and gets typed, cited, source-linked results.
5. As more agents use it, recall tuning compounds — the system gets sharper without manual retraining.

---

## Identity and Delegation Model

- Per-agent permissions: which slices of the world model an agent can read or write.
- Per-tenant isolation in the Cloud and on-prem tiers.
- Source attribution on every recall result (so the agent can cite back to a Snowflake row, a PDF page, a Slack message).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install cognee` |
| 28+ connectors | Snowflake, Postgres, files, REST, Slack, … |
| MCP server | First-party |
| Framework adapters | Claude Code, Codex, Cursor, LangGraph, CrewAI, Continue, Hermes, OpenClaw |
| Cloud + On-Prem tiers | Free local; paid hosted; enterprise on-prem |

---

## Human-in-the-Loop Support

Out of scope for the memory plane itself; compose with HumanLayer / Inferable if certain ingestion or recall events should require approval. Cognee provides the audit trail; HITL is layered on top.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain vector DB** | No ontology, no graph, no recall tuning, no agent permissions; agent owns everything |
| **Mem0 / Zep / MemMachine** | Conversation-memory shaped; Cognee is shaped around an agent's *world* (warehouses, docs, APIs) and builds a managed graph from heterogeneous sources |
| **Hand-rolled GraphRAG** | High operational cost; no compounding recall tuning; no framework adapters; no MCP out of the box |

---

## Use Cases

- **Vertical agent shipped to customers** — Cognee learns the domain (medical research, K-5 special-ed, pharma R&D) once, then any agent runtime queries it
- **Replace scattered RAG** — point Cognee at warehouse + vectors + docs; one `cognee.search` replaces a stack of bespoke retrievers
- **Multi-agent shared world** — one cognified knowledge base, many agents with permissioned slices

---

## Production Notes

- Used by Bayer R&D (compressing 10,000 scientific papers into research memory), Knowunity (40,000 students), and University of Wyoming (K-5 special-ed research with citations).
- Free local development; Cloud tier from $35/mo dev → $200/mo team; enterprise on-prem.
- SOC 2 ready.
