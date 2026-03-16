# Zep

> **"The memory layer for production AI agents — powered by a temporal knowledge graph."**

| | |
|---|---|
| **Website** | https://www.getzep.com |
| **Docs** | https://help.getzep.com |
| **GitHub** | https://github.com/getzep/zep |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/getzep/zep?style=social)](https://github.com/getzep/zep) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Research** | arxiv.org/abs/2501.13956 — Temporal Knowledge Graph Architecture |

---

## Official Website

https://www.getzep.com

---

## Official Repo

https://github.com/getzep/zep — Core platform (open-source)

https://github.com/getzep/zep-python — Python SDK

https://github.com/getzep/zep-js — TypeScript SDK

---

## Agent Skills

**Status:** ⚠️ No official skill published by Zep yet.

```bash
npx clawhub@latest search zep memory
```

---

## MCP

**Status:** ✅ Available

Zep provides an MCP server enabling agents to read and write from the temporal knowledge graph directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Docs** | https://help.getzep.com/mcp |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Zep is an agent memory service built on **Graphiti** — a temporal knowledge graph that automatically synthesizes conversational data and business data into a persistent, evolving knowledge structure. Unlike vector-only memory stores, Zep tracks how facts, preferences, and relationships change over time, maintaining historical records while marking outdated information invalid.

Agents query Zep with a single API call; Zep assembles the most relevant memories, facts, entities, and temporal context and returns a structured context object ready for injection into the agent's prompt.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product page: *"Agent Memory"* — the product is named and positioned exclusively for AI agents; website headline: *"Memory for production AI agents"* |
| **Agent-specific primitive** | Temporal knowledge graph (not just a vector store); automatic fact invalidation over time; custom graph ontologies using Pydantic/Zod; fusion of chat and business data in one API call |
| **Autonomy-compatible control plane** | Sub-200ms P95 retrieval; agents query and update memory autonomously; no human curates the graph |
| **M2M integration surface** | Python SDK, TypeScript SDK, Go SDK, REST API, MCP server |
| **Identity / delegation** | Per-user and per-session graph namespacing; temporal context with date ranges per fact |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Temporal Knowledge Graph** | A graph where every fact has a validity period — outdated facts are marked invalid, not deleted |
| **Graphiti** | The underlying engine that dynamically synthesizes unstructured conversation + structured business data |
| **Entity Tracking** | Automatically extracts and relates entities (people, companies, concepts) from conversations |
| **Temporal Context** | Each fact stored with start/end date ranges — agents know when something was true |
| **Graph Ontology** | Define custom entity types and relationships using Pydantic or Zod schemas |
| **Business Data Fusion** | Load structured CRM/database data into the same graph as conversational memory |
| **Context Assembly** | Single API call returns a complete, structured context window ready for injection |

---

## Autonomy Model

```
Agent calls zep.add_session_message(session_id, message) after each turn
    ↓
Graphiti extracts entities, facts, and relationships from the message
    ↓
New facts compared against existing graph — valid/invalid determined by timestamp
    ↓
Agent calls zep.search(session_id, query) before generating next response
    ↓
Zep assembles temporal context: current facts, entities, changed preferences
    ↓
Agent injects structured context into prompt — no raw history, no token waste
```

---

## Identity and Delegation Model

- `session_id` namespaces the knowledge graph per conversation
- `user_id` namespaces long-term memory per user across sessions
- Temporal validity ranges mean agents always receive the most current version of facts
- Custom ontologies allow per-deployment entity schemas (e.g., a healthcare app vs. a sales app)

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install zep-python` |
| TypeScript SDK | `npm install @getzep/zep-js` |
| Go SDK | `go get github.com/getzep/zep-go` |
| REST API | Full graph management and memory query |
| MCP Server | Direct LLM memory access via Model Context Protocol |

---

## Performance Benchmarks

| Benchmark | Zep | MemGPT |
|---|---|---|
| LongMemEval accuracy | +18.5% improvement | Baseline |
| Token usage | <2% of baseline | Full context |
| P95 retrieval latency | <200ms | N/A |

---

## Human-in-the-Loop Support

None required. Zep manages all memory lifecycle decisions. Humans can inspect the knowledge graph via dashboard for debugging, but no human curation is needed for normal operation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain vector database (Pinecone, Weaviate)** | No temporal tracking, no automatic fact invalidation, no business data fusion; agents must write all extraction and lifecycle logic |
| **Redis** | Key-value store; no graph, no temporal semantics, no context assembly |
| **Mem0** | Extraction-based memory (ADD/UPDATE/DELETE pattern); Zep's temporal knowledge graph provides richer relational context and temporal reasoning |
| **Full context injection** | Exponentially expensive; misses the temporal invalidation of stale facts |

---

## Use Cases

- **Long-running personal assistants** — remember user preferences and how they've changed over months
- **Sales agents** — track company relationships, meeting history, and deal progression over time
- **Healthcare agents** — maintain longitudinal patient context with temporal validity of diagnoses and medications
- **Customer service agents** — remember past issues and resolutions; detect when previous fixes are no longer valid
- **Research agents** — build a knowledge graph of discovered entities and their relationships across multi-session research
