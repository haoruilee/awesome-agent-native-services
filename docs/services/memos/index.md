---
title: "MemOS | Agent-Native Services"
service_name: "MemOS"
description: "A memory OS for LLM and AI agent systems"
permalink: /services/memos/
page_kind: service
service_slug: "memos"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memos.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memos.md"
tagline: "A memory OS for LLM and AI agent systems"
website: "https://openmem.net"
repository: "https://github.com/MemTensor/MemOS"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache 2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openmem.net" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://memos-docs.openmem.net" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/MemTensor/MemOS" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memos.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MemOS is a **memory operating system** — it manages memory as a system resource for AI agents the way an OS manages memory for processes. Rather than treating agent memory as a simple key-value store or vector database, MemOS unifies three fundamentally different types of memory under one API:

- **Parametric memory** — knowledge embedded in model weights
- **Activation memory** — precomputed KV-caches and hidden states for fast context retrieval
- **Plaintext memory** — searchable, editable text, documents, and graph nodes

The basic unit is the **MemCube**: a composable memory object with content, provenance, versioning, and lifecycle metadata. MemCubes can be composed, migrated, and fused as the agent accumulates knowledge.

**MemOS v2.0 benchmark (March 2026):** +43.70% accuracy vs. OpenAI Memory, 35.24% token savings.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST
- **Catalog protocols:** Agent Skill, MCP, REST, SDK, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official OpenClaw plugin available
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK / REST

```bash
pip install memos-core

# Configure and start MemOS
from memos import MemOS
memory = MemOS(config="~/.memos/config.yaml")

# Add a memory from agent session
memory.add("User prefers Python over TypeScript for new projects")

# Retrieve relevant memories before agent responds
results = memory.get("user coding preferences")
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memos.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memos-core` |
| REST API | Full memory CRUD and retrieval |
| MCP Server | stdio / HTTP |
| OpenClaw Plugin | `MemOS-Cloud-OpenClaw-Plugin` at github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
