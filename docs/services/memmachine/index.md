---
title: "MemMachine | Agent-Native Services"
service_name: "MemMachine"
description: "Universal memory layer for AI Agents. Scalable, extensible, and interoperable memory storage and retrieval for next-generation autonomous systems"
permalink: /services/memmachine/
page_kind: service
service_slug: "memmachine"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memmachine.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmachine.md"
tagline: "Universal memory layer for AI Agents. Scalable, extensible, and interoperable memory storage and retrieval for next-generation autonomous systems"
website: "https://memmachine.ai"
repository: "https://github.com/MemMachine/MemMachine"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Planned</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://memmachine.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.memmachine.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/MemMachine/MemMachine" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmachine.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MemMachine is a long-term memory layer for AI agents that explicitly composes **three memory types** as separate, interoperable subsystems:

1. **Episodic memory** — graph-backed conversational context (who said what, in what order, with what relationships).
2. **Profile memory** — SQL-backed user / agent facts (durable, queryable, deduplicated).
3. **Working memory** — short-term scratchpad scoped to the current run.

This three-layer model is the differentiator from one-bucket memory layers: episodic graph traversal answers "what happened in the conversation?", profile SQL answers "what do we know about this user?", and working memory is the running scratchpad that flushes to the other two on a schedule. The library is framework-agnostic but ships first-class adapters for LangChain and CrewAI.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, API
- **MCP:** ⚠️ MCP server is on the roadmap; community wrappers exist. Primary surface is SDK + REST.
- **Agent Skill:** ⚠️ Not yet published as an official skill.
- **Onboarding type:** `sdk`

## How agents onboard

```
pip install memmachine
# then:
from memmachine import Memory
m = Memory()
m.add(messages, agent_id=...)
context = m.recall(query, agent_id=...)
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmachine.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memmachine` |
| LangChain adapter | In-tree |
| CrewAI adapter | In-tree |
| REST API | For non-Python agents |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
