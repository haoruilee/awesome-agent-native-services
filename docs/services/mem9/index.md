---
title: "mem9 | Agent-Native Services"
service_name: "mem9"
description: "Persistent memory for AI agents"
permalink: /services/mem9/
page_kind: service
service_slug: "mem9"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/mem9.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem9.md"
tagline: "Persistent memory for AI agents"
website: "https://mem9.ai"
repository: "https://github.com/mem9-ai/mem9"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache 2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mem9.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/mem9-ai/mem9" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem9.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

mem9 is **cloud-persistent memory infrastructure for AI agents** — solving the problem of agents forgetting context between sessions. Memory survives resets, restarts, and machine switches. Hybrid search combines vector similarity and keyword search with zero configuration. Cross-agent memory sharing lets agents on different platforms (Claude Code, OpenCode, OpenClaw) access the same memory pool.

Zero-ops setup: instant deployment without schema design or database management. Auto-embedding via `EMBED_TEXT()` generates embeddings server-side without requiring OpenAI keys.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.
- **Catalog protocols:** URL onboarding, Agent Skill, REST, http, API
- **MCP:** ⚠️ Not yet published (REST API primary; plugins for OpenClaw, Claude Code, OpenCode)
- **Agent Skill:** ✅ URL Onboarding via skill.md — agent reads https://mem9.ai/skill.md and follows instructions
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.

```
Read https://mem9.ai/skill.md and follow the instructions to register and join.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem9.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://api.mem9.ai/v1alpha2/mem9s/memories` — CRUD, search, import |
| OpenClaw Plugin | `@mem9/mem9` — 5 tools + lifecycle hooks |
| Claude Code / OpenCode | Native plugins with same 5 tools |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
