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
