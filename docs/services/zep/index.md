---
title: "Zep | Agent-Native Services"
service_name: "Zep"
description: "The memory layer for production AI agents — powered by a temporal knowledge graph"
permalink: /services/zep/
page_kind: service
service_slug: "zep"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/zep.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zep.md"
tagline: "The memory layer for production AI agents — powered by a temporal knowledge graph"
website: "https://www.getzep.com"
repository: "https://github.com/getzep/zep"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.getzep.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://help.getzep.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/getzep/zep" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zep.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Zep is an agent memory service built on **Graphiti** — a temporal knowledge graph that automatically synthesizes conversational data and business data into a persistent, evolving knowledge structure. Unlike vector-only memory stores, Zep tracks how facts, preferences, and relationships change over time, maintaining historical records while marking outdated information invalid.

The open-source Graphiti framework is listed separately as [Graphiti](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md) (`getzep/graphiti`). This Zep entry is the managed product/platform (`getzep/zep`). Do not treat them as one service.

Agents query Zep with a single API call; Zep assembles the most relevant memories, facts, entities, and temporal context and returns a structured context object ready for injection into the agent's prompt.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official skill published by Zep yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install zep-python` |
| TypeScript SDK | `npm install @getzep/zep-js` |
| Go SDK | `go get github.com/getzep/zep-go` |
| REST API | Full graph management and memory query |
| MCP Server | Direct LLM memory access via Model Context Protocol |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
