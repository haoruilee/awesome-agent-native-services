---
title: "GoodMem | Agent-Native Services"
service_name: "GoodMem"
description: "Memory that survives context windows"
permalink: /services/goodmem/
page_kind: service
service_slug: "goodmem"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/goodmem.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/goodmem.md"
tagline: "Memory that survives context windows"
website: "https://goodmem.ai/"
repository: "https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://goodmem.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.goodmem.ai/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/goodmem.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

GoodMem gives agents persistent, searchable memory outside their context windows. Agents store documents, prior findings, and task history in memory spaces. The service handles configured chunking and embedding, then retrieves relevant context with optional reranking. Spaces can be isolated for one workload or shared between authorized agents. See the [integration overview](https://docs.goodmem.ai/docs/integrations/).

**Dual-use boundary:** GoodMem also supports conventional RAG, including document Q&A and knowledge search. Its storage and retrieval APIs are useful to ordinary applications as well as agents; those APIs are not exclusively agent-specific. This entry covers the persistent agent-memory workflow, published MCP/skills, and workload identity model. It does not claim automatic conversation-fact extraction, conflict resolution, or autonomous forgetting merely from storing a memory.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (Streamable HTTP)
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, STDIO, http, API
- **MCP:** ✅ Available through two distinct interfaces.
- **Agent Skill:** ✅ Available in the official Claude Code plugin.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (Streamable HTTP)

```json
{
  "mcpServers": {
    "goodmem": {
      "url": "https://goodmem.example.com/mcp",
      "headers": {
        "x-api-key": "gm_your_key"
      }
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/goodmem.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Memory, space, model, and access-control operations; see the [API reference](https://docs.goodmem.ai/docs/reference/api-reference/) |
| gRPC | Available for self-hosted deployments; GoodMem Cloud does not expose gRPC |
| Language SDKs | SDK access to GoodMem; the plugin includes a Python SDK skill |
| CLI | Structured commands for provisioning and operations; the service-identity guide documents workload setup |
| Native MCP | Built-in Streamable HTTP at `/mcp`; read-only retrieval and diagnostics |
| Stdio MCP adapter | Published npm server with additional ingestion and management operations |
| Framework integrations | [LlamaIndex and other integrations](https://docs.goodmem.ai/docs/integrations/) for memory ingestion and retrieval |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
