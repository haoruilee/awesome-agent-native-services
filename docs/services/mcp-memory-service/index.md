---
title: "mcp-memory-service | Agent-Native Services"
service_name: "mcp-memory-service"
description: "Memory for AI Agents — REST, MCP, OAuth, CLI"
permalink: /services/mcp-memory-service/
page_kind: service
service_slug: "mcp-memory-service"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/mcp-memory-service.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mcp-memory-service.md"
tagline: "Memory for AI Agents — REST, MCP, OAuth, CLI"
verified_at: "2026-10-20"
website: "https://mcpmemory.services"
repository: "https://github.com/doobidoo/mcp-memory-service"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mcpmemory.services" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mcpmemory.services" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/doobidoo/mcp-memory-service" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mcp-memory-service.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

mcp-memory-service is a **self-hosted memory backend** for AI agent pipelines: one process exposes REST, MCP, OAuth, CLI, and a dashboard. Agents store decisions, share a causal knowledge graph (typed edges: causes, fixes, contradicts), retrieve in ~5 ms, and run autonomous consolidation — embeddings stay local (ONNX) unless the operator chooses a cloud backend.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [Zep](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zep.md) / [Graphiti](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md) | Temporal context-graph product vs OSS Graphiti framework. This entry is a multi-transport memory *service* (REST+MCP+OAuth) with `X-Agent-ID` |
| [Mem0](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem0.md) | Extraction SDK/SaaS. mcp-memory-service is self-host MCP+REST with OAuth DCR |
| [Recall](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/recall.md) | MCP-native self-host memory — narrower transport set, no OAuth/DCR story |
| [MemPalace](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md) | Palace/drawer metaphor + 44 MCP tools. Different architecture (README compares LongMemEval claims) |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP / REST
- **Catalog protocols:** MCP, REST, CLI, STDIO, http
- **MCP:** ✅ Available — the service is an MCP memory server (stdio + Streamable HTTP + SSE)
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP / REST

```bash
pip install mcp-memory-service
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mcp-memory-service.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| PyPI | `pip install mcp-memory-service` |
| CLI | `memory server` / `memory server --http` |
| REST | `:8000` — 76 endpoints |
| MCP | stdio + Streamable HTTP + SSE |
| OAuth | 2.0 + DCR for remote MCP |
| License | Apache-2.0 |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/doobidoo/mcp-memory-service

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
