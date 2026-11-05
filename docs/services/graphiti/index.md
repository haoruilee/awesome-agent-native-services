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
