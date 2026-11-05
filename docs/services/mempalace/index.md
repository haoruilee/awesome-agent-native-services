---
title: "MemPalace | Agent-Native Services"
service_name: "MemPalace"
description: "The best-benchmarked open-source AI memory system. And it's free"
permalink: /services/mempalace/
page_kind: service
service_slug: "mempalace"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/mempalace.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md"
tagline: "The best-benchmarked open-source AI memory system. And it's free"
verified_at: "2026-10-13"
website: "https://mempalaceofficial.com"
repository: "https://github.com/MemPalace/mempalace"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mempalaceofficial.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mempalaceofficial.com/guide/getting-started.html" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/MemPalace/mempalace" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MemPalace is a local-first memory system for AI agents. It stores conversation history as **verbatim text** and retrieves it with semantic search. Official copy: it does not summarize, extract, or paraphrase. The index is a palace metaphor — people and projects are *wings*, topics are *rooms*, original content lives in *drawers* — so searches can be scoped instead of run against a flat corpus.

The retrieval backend is pluggable (ChromaDB default; SQLite exact, Milvus, Qdrant, and pgvector are documented). Nothing leaves the machine unless the operator opts in. A temporal entity-relationship graph with validity windows sits on local SQLite. Each specialist agent can get its own wing and diary, discoverable at runtime via `mempalace_list_agents`.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP
- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP

```bash
uv tool install mempalace
mempalace init ~/projects/myapp
mempalace mine ~/projects/myapp
mempalace search "why did we switch to GraphQL"
mempalace wake-up
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `uv tool install mempalace` then `init`, `mine`, `search`, `wake-up` |
| Python API | `pip install mempalace` inside a venv |
| MCP stdio | Local CLI or `docker run -i ghcr.io/mempalace/mempalace` |
| Docker | `ghcr.io/mempalace/mempalace:latest`; data under `/data` |
| Docs | [Getting started](https://mempalaceofficial.com/guide/getting-started.html), [MCP tools](https://mempalaceofficial.com/reference/mcp-tools.html) |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/MemPalace/mempalace

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
