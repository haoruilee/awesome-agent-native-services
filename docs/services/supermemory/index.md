---
title: "Supermemory | Agent-Native Services"
service_name: "Supermemory"
description: "The Memory API for the AI era"
permalink: /services/supermemory/
page_kind: service
service_slug: "supermemory"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/supermemory.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/supermemory.md"
tagline: "The Memory API for the AI era"
verified_at: "2026-10-30"
website: "https://supermemory.ai"
repository: "https://github.com/supermemoryai/supermemory"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://supermemory.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://supermemory.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/supermemoryai/supermemory" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/supermemory.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

### Two credentials, one store

Access is handed out two different ways, and the dossier documents only one of them in detail. The hosted MCP endpoint at `https://mcp.supermemory.ai/mcp` uses OAuth: the client opens a consent page once, and the owner picks which spaces that client may read or write. No API key sits in the client config. The Memory API and SDKs take an API key instead, and the dossier does not say whether such a key can be limited to particular spaces the way an OAuth grant is. Self-hosting gets one line, an MIT monorepo that can run fully locally, with no word on whether the OAuth flow and console come along. The [Supermemory docs](https://supermemory.ai/docs) are where both answers should be.

The repository ships a `skills/` directory, but no install command is documented, so the catalog leaves the Agent Skill status as unknown.

### Spaces and profiles

What the dossier does document is a memory engine with a clear tool contract. An agent saves facts and documents with `add_memory`, and the engine extracts versioned memories. A later session, in the same or a different MCP client, recalls them with `search_memory`, which returns memories with their source document IDs. `get_profile` returns stable and recent facts for the active space, and a `context` prompt primes a new session with them. `forget_memory` removes a memory by ID or by exact content.

Spaces are the isolation boundary. Reads and writes go to the active space unless a `namespace` targets another permitted one, so several assistants can share a project's memory without mixing in unrelated work. `who_am_i` reports the client's identity, role, and scope, and each connected app can be revoked from the console's Agents page.

A person can stay out of the loop entirely, or use the `guided-save` widget to edit a memory before it is stored.

### Shared memory elsewhere in the category

[Memory & State](/categories/memory-and-state/) holds several stores with different shapes, compared in [Memory layers for agents](/guides/memory-layers-for-agents/). [Mem0](/services/mem0/) calls itself the memory layer for your agents, the closest pitch. [Zep](/services/zep/) and [Graphiti](/services/graphiti/) attach time to facts through a knowledge graph. [Memoria](/services/memoria/) offers Git-level version control over memory. The tagline, "The Memory API for the AI era.", undersells the part the dossier spends most time on: per-client grants and spaces, which turn it into memory shared across assistants.

### Editor's take

Supermemory fits someone who works across several AI clients and wants one project memory they all read, with consent granted per client rather than a shared key copied between configs. Teams that need reasoning about when facts changed should compare Zep, and teams that want history on every edit should look at Memoria. This is our reading of the dossier and the vendor's MCP documentation; we have not connected a client to it.

</section>

## What it does

Supermemory is a memory and context engine for AI assistants and agents. Agents save facts and documents, the engine extracts versioned memories, and later sessions (in any MCP client) recall them by semantic search or a stable profile. Spaces keep each project's memories separate, so a single agent or a team of assistants can share context without mixing unrelated work.

---

## Agent-facing interfaces

- **Interaction pattern:** Remote MCP + REST API / SDK
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Available — hosted remote MCP (Streamable HTTP) with OAuth.
- **Agent Skill:** ⚠️ The repository ships a skills/ directory; no single published npx skills add command is documented on the MCP page.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Remote MCP + REST API / SDK

```json
{ "mcpServers": { "supermemory": { "url": "https://mcp.supermemory.ai/mcp" } } }
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/supermemory.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.supermemory.ai/mcp` |
| REST API / SDKs | https://supermemory.ai/docs |
| Self-host | MIT monorepo, can run fully locally |

---

## Verification

Last verified **2026-10-30**.

Sources:
- https://api.github.com/repos/supermemoryai/supermemory

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
