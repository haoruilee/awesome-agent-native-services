---
title: "memU | Agent-Native Services"
service_name: "memU"
description: "Memory for 24/7 proactive AI agents"
permalink: /services/memu/
page_kind: service
service_slug: "memu"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memu.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memu.md"
tagline: "Memory for 24/7 proactive AI agents"
website: "https://memu.pro"
repository: "https://github.com/NevaMind-AI/memU"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://memu.pro" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://memu.pro/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/NevaMind-AI/memU" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memu.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

memU is a **persistent memory framework specifically built for 24/7 proactive AI agents** — agents that run continuously, monitor data streams, and act without explicit user commands. The critical insight: most agent memory systems are optimized for interactive sessions, but proactive agents need memory that works at *millisecond* latency while the agent is idle, only invoking expensive LLM reasoning when something truly relevant is detected.

memU solves this with **dual-mode retrieval**:
- **Fast Context (RAG mode)** — embedding-based monitoring running continuously, sub-millisecond latency, near-zero cost
- **Deep Reasoning (LLM mode)** — full LLM capabilities activated only when Fast Context detects a relevant pattern

The agent saves ~90% of token costs because expensive LLM reasoning only fires when the lightweight monitor says "this matters."

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST
- **Catalog protocols:** REST, SDK, API
- **MCP:** ⚠️ Not yet published as standalone MCP server.
- **Agent Skill:** ⚠️ No official skill published yet.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK / REST

```bash
pip install memu

# Initialize memory layer
from memu import MemU
memory = MemU(agent_id="my-agent")

# Continuous monitoring mode — for proactive 24/7 agents
memory.monitor(data_stream=my_stream, callback=on_relevant_event)

# Or: standard add/retrieve
memory.add(content="User has deadline on Friday")
context = memory.retrieve("user schedule and priorities")
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memu.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memu` |
| REST API | Memory CRUD, stream monitoring, context retrieval |
| OpenClaw Integration | Native plugin for OpenClaw memory sessions |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
