---
title: "Graphiti | Agent-Native Services"
service_name: "Graphiti"
description: "Build Real-Time Knowledge Graphs for AI Agents"
permalink: /services/graphiti/
page_kind: service
service_slug: "graphiti"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/graphiti.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md"
tagline: "Build Real-Time Knowledge Graphs for AI Agents"
verified_at: "2026-10-20"
website: "https://help.getzep.com/graphiti"
repository: "https://github.com/getzep/graphiti"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · STDIO</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://help.getzep.com/graphiti" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://help.getzep.com/graphiti" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/getzep/graphiti" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

### Everything is yours to hold

No service stands behind Graphiti. It is an Apache-2.0 Python framework, and the dossier is explicit that the credentials are the operator's: LLM API keys for extraction and the graph database login, both of which the MCP server inherits from its environment. There are no hosted users, threads, or API keys; those belong to the managed [Zep](/services/zep/) product. What the dossier does not settle is the MCP server's maturity. Graphiti's own docs call it experimental, and it starts from a cloned repository rather than an installed package. Read the [Graphiti docs](https://help.getzep.com/graphiti) on its current state before wiring an assistant to it.

No official Agent Skill has been published either.

### Episodes in, facts out

The documented model starts with an episode: a piece of text, a message, or JSON that the agent adds. Graphiti extracts entities and facts from it, and every fact carries a validity window and a pointer back to the episode that produced it. New episodes update the graph incrementally, and older facts that no longer hold are invalidated rather than recomputed in a batch. Retrieval mixes semantic search, BM25 keyword search, and graph traversal.

After `pip install graphiti-core`, the dossier shows `from graphiti_core import Graphiti`, a Neo4j driver passed in as `graph_driver`, then `add_episode(...)` and `search(...)`. Neo4j, FalkorDB, Kuzu, and Neptune are the supported backends. Custom entity and edge types are Pydantic models, and a `group_id` separates graphs per user or project.

The MCP server runs with `uv run graphiti_mcp_server.py`, over stdio for Claude Desktop or SSE for Cursor, and a Docker Compose file starts it together with a database. Its tools include `add_episode`, `search_facts`, `search_nodes`, and `clear_graph`.

### Not the same entry as Zep

[Memory & State](/categories/memory-and-state/) keeps Graphiti and Zep apart deliberately. Zep is the managed service with its own engine and dashboard; Graphiti is the open framework you run. [Cognee](/services/cognee/) also builds graphs, but from warehouses, documents, and APIs rather than episodes. [Recall](/services/recall/) is open-source, MCP-native, and self-hosted as well, so it is the other entry to read if running your own memory is the requirement. [Mem0](/services/mem0/) calls itself the memory layer for your agents. The tagline here is "Build Real-Time Knowledge Graphs for AI Agents". The [Memory layers for agents](/guides/memory-layers-for-agents/) guide sets the approaches next to each other.

### Editor's take

Graphiti is for teams that want temporal memory, already run or are willing to run a graph database, and want to read every line of the engine. If you would rather not operate Neo4j and an extraction pipeline, Zep packages the same lineage as a service. Our account reflects the dossier and Graphiti's public docs; we have not built a graph with it.

</section>

## What it does

Graphiti is Zep’s **open-source framework** for temporal knowledge graphs (Context Graphs). Agents ingest episodes (text, messages, JSON); Graphiti extracts entities and facts with **validity windows**, incremental updates (no batch recomputation), provenance back to source episodes, and hybrid retrieval (semantic + BM25 + graph traversal).

It is the engine described in [arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956). Operators bring Neo4j, FalkorDB, Kuzu, or Neptune.

**Distinct from [Zep](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zep.md):** Zep is the production memory *product* (users/threads, sub-200 ms managed retrieval, dashboard, SLAs). Graphiti is the OSS library + MCP you self-host. Cross-link only; do not collapse them.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + MCP
- **Catalog protocols:** MCP, SDK, STDIO
- **MCP:** ✅ Available — in-repo Graphiti MCP Server (docs call it experimental)
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK + MCP

```bash
pip install graphiti-core
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install graphiti-core` (+ extras: `falkordb`, `kuzu`, `neptune`, `anthropic`, …) |
| MCP | `uv run graphiti_mcp_server.py` — stdio or SSE |
| Docker | `mcp_server` Compose (DB + MCP) |
| Paper | arxiv.org/abs/2501.13956 |
| License | Apache-2.0 |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/getzep/graphiti

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
