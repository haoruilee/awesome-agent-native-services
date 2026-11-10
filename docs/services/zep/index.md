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

<section class="service-essay" aria-label="Editorial" markdown="1">

### Open repository, managed product

Two catalog records disagree on how open Zep is. The Zep dossier lists `getzep/zep` as the open-source core platform. The Graphiti dossier, citing the official README, describes Zep as managed infrastructure on a proprietary Context Graph Engine, with Graphiti as the open framework you host yourself. Neither record describes a self-hosted Zep deployment. Plan on Zep being a service someone else runs unless the [Zep docs](https://help.getzep.com) say otherwise for your case, and read the data handling terms on that basis.

The dossier lists no official Agent Skill. The MCP server is documented with a stdio transport, so it runs beside the client and calls Zep with your key.

### Facts with dates

The documented idea is a temporal knowledge graph. After each turn the agent adds the message. Graphiti, the engine underneath, extracts entities, facts, and relationships and compares them against what the graph already holds. When a fact changes, the old one is marked invalid with a date range instead of being deleted. Before the next response, the agent searches and gets back an assembled context object of current facts, entities, and changed preferences, ready to drop into a prompt.

The calls shown are `zep.add_session_message(...)` and `zep.search(...)`, after `pip install zep-python`. TypeScript and Go SDKs and a REST API are listed as well. A `session_id` scopes a conversation and a `user_id` scopes long-term memory across sessions. Custom entity and relationship types can be defined with Pydantic or Zod, and structured business data such as CRM records can be loaded into the same graph as conversation.

No person curates the graph. A dashboard exists for inspection and debugging.

### Among memory services

The [Memory & State](/categories/memory-and-state/) category keeps Zep and [Graphiti](/services/graphiti/) apart on purpose: same lineage, different operator. [Mem0](/services/mem0/) is the comparison the Zep dossier draws itself, describing it as add, update, and delete extraction without temporal reasoning. [Cognee](/services/cognee/) builds a graph from warehouses and documents rather than conversation. [Supermemory](/services/supermemory/) separates memories into spaces. The tagline, "The memory layer for production AI agents — powered by a temporal knowledge graph.", is the vendor's framing. The [Memory layers for agents](/guides/memory-layers-for-agents/) guide walks through the alternatives.

### Editor's take

Zep is the choice for assistants whose users change their minds over months, where knowing when something stopped being true matters as much as the fact itself, and where a managed service is acceptable. Teams that need the same model on their own database should go to Graphiti directly and accept running it. Everything here is drawn from two catalog files and Zep's help center; no session was written to Zep while preparing it.

</section>

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
