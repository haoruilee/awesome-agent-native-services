# Graphiti

> **"Build Real-Time Knowledge Graphs for AI Agents"**

| | |
|---|---|
| **Website** | https://help.getzep.com/graphiti |
| **Docs** | https://help.getzep.com/graphiti |
| **GitHub** | https://github.com/getzep/graphiti |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/getzep/graphiti?style=social)](https://github.com/getzep/graphiti) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/getzep/graphiti)); PyPI `graphiti-core`; MCP server in-repo |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://help.getzep.com/graphiti

Docs welcome (live 2026-09-04): **“Welcome to Graphiti!”** Supporting line: “Graphiti is Zep's open-source framework for temporal knowledge graphs — Context Graphs — for AI agents, with real-time updates and hybrid retrieval.”

---

## Official Repo

https://github.com/getzep/graphiti

GitHub description (catalog tagline, live 2026-09-04): **“Build Real-Time Knowledge Graphs for AI Agents”**

README subtitle: **“A Framework for Building Temporal Knowledge Graphs”**. Body: “Graphiti is a framework for building and querying temporal context graphs for AI agents.”

**Not the same entry as [Zep](zep.md).** Graphiti is the OSS temporal-graph framework + MCP. Zep is the managed context-graph product/platform (`getzep/zep`). Official README table: Graphiti = self-hosted framework, bring your own graph DB; Zep = managed infrastructure with a proprietary Context Graph Engine. Do not merge the rows.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + MCP

```bash
pip install graphiti-core
```

```python
from graphiti_core import Graphiti
from graphiti_core.driver.neo4j_driver import Neo4jDriver

driver = Neo4jDriver(...)
graphiti = Graphiti(graph_driver=driver)
await graphiti.add_episode(...)
results = await graphiti.search(...)
```

MCP server (official docs: [Graphiti MCP Server](https://help.getzep.com/graphiti/getting-started/mcp-server)):

```bash
git clone https://github.com/getzep/graphiti.git
cd graphiti/mcp_server
uv sync
uv run graphiti_mcp_server.py
```

Docker: `docker compose up` in `mcp_server` (FalkorDB or Neo4j + SSE). There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search graphiti
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — in-repo Graphiti MCP Server (docs call it experimental)

| Detail | Value |
|---|---|
| **MCP Docs** | https://help.getzep.com/graphiti/getting-started/mcp-server |
| **MCP Repo** | https://github.com/getzep/graphiti/tree/main/mcp_server |
| **Transport** | stdio (Claude Desktop) / SSE (`http://localhost:8000/sse` for Cursor) |
| **Tools** | `add_episode`, `search_facts`, `search_nodes`, `get_episodes`, `delete_episode`, `clear_graph` |
| **Compatible Clients** | Claude Desktop, Cursor, VS Code + Copilot, any MCP client |
| **Docs MCP** | https://help.getzep.com/_mcp/server (documentation only) |

---

## What It Does

Graphiti is Zep’s **open-source framework** for temporal knowledge graphs (Context Graphs). Agents ingest episodes (text, messages, JSON); Graphiti extracts entities and facts with **validity windows**, incremental updates (no batch recomputation), provenance back to source episodes, and hybrid retrieval (semantic + BM25 + graph traversal).

It is the engine described in [arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956). Operators bring Neo4j, FalkorDB, Kuzu, or Neptune.

**Distinct from [Zep](zep.md):** Zep is the production memory *product* (users/threads, sub-200 ms managed retrieval, dashboard, SLAs). Graphiti is the OSS library + MCP you self-host. Cross-link only; do not collapse them.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub description: **“Build Real-Time Knowledge Graphs for AI Agents”** — [getzep/graphiti](https://github.com/getzep/graphiti). Docs: temporal knowledge graphs “for AI agents.” |
| **Agent-specific primitive** | Temporal facts with validity windows; episodes + provenance; prescribed/learned ontology; `group_id` multi-tenant graphs; hybrid search |
| **Autonomy-compatible control plane** | After a graph driver is up, agents `add_episode` / `search` (SDK or MCP) with no human curation |
| **M2M integration surface** | `graphiti-core` Python SDK, MCP server (stdio/SSE), Docker Compose |
| **Identity / delegation** | `group_id` namespaces graphs per user/project; episode provenance; no hosted KYA — C5 is graph namespace + operator DB credentials |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Episode** | Raw ingest unit; every derived fact traces back here |
| **Temporal fact / edge** | Triplet with valid-from / invalid-at windows |
| **Entity node** | People, products, concepts — summaries evolve |
| **Hybrid retrieval** | Semantic + keyword + graph walk |
| **Custom ontology** | Pydantic entity and edge types |
| **`group_id`** | Isolate graphs across users or agents |

---

## Autonomy Model

```
Operator provisions Neo4j/FalkorDB/Kuzu/Neptune and installs graphiti-core (or MCP)
    -> Agent add_episode after each turn or tool result
    -> Graphiti incrementally updates entities/facts and invalidates stale edges
    -> Agent search / MCP search_facts before the next LLM call
    -> Structured temporal context returns; no dashboard required
```

---

## Identity and Delegation Model

- **Graph namespace:** `group_id` (MCP) / driver-level isolation per deployment.
- **Provenance:** every fact points at the episode that produced it.
- **Caller credentials:** operator-held LLM API keys and graph-DB auth; MCP inherits that env.
- **Zep Cloud identity** (users, threads, API keys) lives on the [Zep](zep.md) product, not in this OSS framework.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install graphiti-core` (+ extras: `falkordb`, `kuzu`, `neptune`, `anthropic`, …) |
| MCP | `uv run graphiti_mcp_server.py` — stdio or SSE |
| Docker | `mcp_server` Compose (DB + MCP) |
| Paper | arxiv.org/abs/2501.13956 |
| License | Apache-2.0 |

---

## Human-in-the-Loop Support

None required for ingest/search. Humans inspect the graph in their own DB tools. Zep’s dashboard is the product surface, not Graphiti.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **[Zep](zep.md)** | Managed product on a proprietary engine. Graphiti is the self-host OSS framework — listed separately on purpose |
| **Mem0 / vector DB** | No bi-temporal fact invalidation or episode provenance |
| **Microsoft GraphRAG** | Batch static summarization; Graphiti is incremental + temporal |
| **Raw Neo4j** | No agent episode ingest, hybrid search recipe, or MCP tool set |

---

## Use Cases

- **Self-host temporal memory** — agents that need “what is true now vs then”
- **MCP assistants** — Claude/Cursor persist context via `add_episode` / `search_facts`
- **Custom ontologies** — domain entity types in Pydantic
- **Research / on-prem** — same paper architecture as Zep without the managed platform
