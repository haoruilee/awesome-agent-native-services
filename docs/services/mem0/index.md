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

<section class="service-essay" aria-label="Editorial" markdown="1">

A long-running agent that stuffs the whole transcript back into the prompt will eventually run out of window, and it will still forget the one fact that mattered. Mem0 is filed as the memory layer that extracts facts, reconciles them with what it already stored, and returns a smaller context at query time. The tagline is "The memory layer for your AI agents." The quick path is `pip install mem0ai` and `m.add(messages, user_id=...)`. The agent calls the API. The dossier says Mem0 decides what to store, update, or retrieve, including conflict handling described as add, update, delete, or no-op. Memory types named are episodic, semantic, and procedural. Namespacing is per user and per agent. A graph mode is mentioned. Docs are [docs.mem0.ai](https://docs.mem0.ai). The repo is [mem0ai/mem0](https://github.com/mem0ai/mem0).

MCP is a separate server, [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp), documented at [docs.mem0.ai/integrations/mcp-server](https://docs.mem0.ai/integrations/mcp-server). The dossier says it exposes the memory operations as tools over stdio, with Docker and Smithery also listed as ways to run it. A community skill, `mem0-memory`, is recorded via `npx skills add`. The catalog marks both the skill and MCP as available. There is also a Python SDK and a REST API. The dossier includes vendor performance and adoption figures. They are not repeated here. If a number matters to a design, read the current docs and treat it as the vendor's claim.

[Memory layers for agents](/guides/memory-layers-for-agents/) separates fact extractors, temporal graphs, shared wikis, and local memory for coding agents. Mem0 is the extractor: automatic write from a conversation, not a page someone edits. [Zep](/services/zep/) is the temporal knowledge graph in the same [Memory & State](/categories/memory-and-state/) collection. [Graphiti](/services/graphiti/) is the real-time knowledge-graph library. [Cognee](/services/cognee/) calls itself a memory control plane. [Letta](/services/letta/), in the runtime collection, keeps state inside the agent deployment, including a self-editing memory pattern. Mem0 is a layer you call, with `user_id` as the scope. [Recall](/services/recall/) is the open-source, MCP-native, self-hosted neighbor if you do not want this API. The guide's warning applies: automatic extraction applies someone else's judgment to the transcript. That is the product, and it is also the failure mode.

### Who writes, and who can read it back

Confirm in the docs what `user_id` isolates, whether an agent id is a second namespace or just a field, and whether the graph mode is on by default. Extraction that silently drops a fact looks like a successful call. The dossier does not show the retrieval payload. Keys are `MEM0_API_KEY` in the skill notes. A key that can read every user's memories is a delegation larger than one agent. Retention and training use of stored text are not settled in the catalog entry. Read them in the vendor policy before you send customer conversations.

### Editor's take

Mem0 fits an agent that should remember facts across sessions and can accept that the service, not the prompt, chooses what is salient. It is a poor fit if you need an explicit graph you edit, which is the Zep and Graphiti conversation, or if the memory must stay on a machine you control. This project has not stored or queried a memory. The opinion is from the SDK quickstart and the MCP docs linked in the dossier, with the vendor's benchmark language left out on purpose.

</section>

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
