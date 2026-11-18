---
title: "Loom | Agent-Native Services"
service_name: "Loom"
description: "Shared memory, document search and code intelligence for AI agents"
permalink: /services/loom/
page_kind: service
service_slug: "loom"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/loom.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/loom.md"
tagline: "Shared memory, document search and code intelligence for AI agents"
website: "https://clickhouse.github.io/loom/"
repository: "https://github.com/ClickHouse/loom"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://clickhouse.github.io/loom/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/ClickHouse/loom/blob/v1.2.0/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ClickHouse/loom" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/loom.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Loom is self-hosted infrastructure for shared agent memory across sessions. `memory.set_from_messages` selects durable facts from transcripts, removes repeated content and writes through conflict checks while preserving source evidence. Agents retrieve memories semantically over MCP, HTTP or SDKs. [Released extraction guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/extraction.md).

Memory lifecycle includes [deduplication and conflict policies](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/conflicts-and-refusal.md), [semantic retrieval](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/search-and-ask.md) and [writer-set expiry or configured retention](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/retention-and-erasure.md). There is no default age-based eviction: removal follows a writer, owner or operator instruction.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP Tool
- **Catalog protocols:** Agent Skill, MCP, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Bundled with the official coding-agent plugin
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP Tool

```json
{
  "url": "https://loom.example.com/mcp?toolset=coding",
  "headers": { "Authorization": "Bearer <JWT>" }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/loom.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | Streamable HTTP tools at `/mcp`. |
| HTTP API | Operations at `POST /v1/<op>`. |
| Python SDK | Programmatic memory operations. |
| TypeScript SDK | Programmatic memory operations. |

Sources: [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md), [MCP client guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/mcp-clients.md).

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
