---
title: "Mem0 | Agent-Native Services"
service_name: "Mem0"
description: "The memory layer for your AI agents"
permalink: /services/mem0/
page_kind: service
service_slug: "mem0"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/mem0.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem0.md"
tagline: "The memory layer for your AI agents"
website: "https://mem0.ai"
repository: "https://github.com/mem0ai/mem0"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mem0.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mem0.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mem0ai/mem0" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem0.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mem0 is a self-improving, adaptive memory layer for AI agents. It automatically extracts salient facts from conversations, reconciles new information with existing memories, and returns only the relevant context at query time — reducing token costs by 90% versus full context injection, while improving answer accuracy by 26% on memory benchmarks.

The agent calls the Mem0 API; Mem0 handles all decisions about what to store, what to update, and what to retrieve. The agent does not manage its own memory.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skill available via the AgentSkills ecosystem
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `mem0.add()`, `mem0.search()`, `mem0.update()`, `mem0.delete()` |
| REST API | Full memory CRUD and search |
| MCP Server | Model Context Protocol for direct LLM memory access |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
