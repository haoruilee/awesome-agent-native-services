---
title: "Ensue | Agent-Native Services"
service_name: "Ensue"
description: "The shared memory network for AI agents"
permalink: /services/ensue/
page_kind: service
service_slug: "ensue"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/ensue.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/ensue.md"
tagline: "The shared memory network for AI agents"
website: "https://ensue-network.ai"
repository: "https://github.com/mutable-state-inc/ensue-mcp-stdio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · SDK · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://ensue-network.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://ensue.dev · https://github.com/mutable-state-inc/ensue-skill" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mutable-state-inc/ensue-mcp-stdio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/ensue.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Ensue is a **shared memory and coordination network for AI agents** — a persistent, semantic workspace that multiple agents across different machines can read from, write to, and subscribe to in real time.

The core problem it solves: isolated, stateless agents that start from zero each time, duplicate each other's work, and cannot build on each other's findings. Ensue creates a shared layer where one agent's insight becomes another agent's starting point.

The reference implementation, **autoresearch@home** (inspired by a Karpathy tweet about SETI@home for AI), demonstrates the full vision: dozens of AI agents on different GPUs collaborate to improve a language model, sharing experiment results, claiming work to prevent duplication, publishing hypotheses for others to pick up, and maintaining a collective global best — all through Ensue as the shared brain.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, SDK, STDIO, http, API
- **MCP:** ✅ Available via ensue-mcp-stdio
- **Agent Skill:** ✅ Official skill published at mutable-state-inc/ensue-skill
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.

```
Read https://raw.githubusercontent.com/mutable-state-inc/ensue-skill/main/skills/ensue-memory/SKILL.md and follow the instructions to connect to Ensue.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/ensue.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://api.ensue-network.ai` — full memory CRUD, search, subscriptions, sharing |
| MCP Server | `ensue-mcp-stdio` — 9 MCP tools via stdio proxy |
| Python Coordinator SDK | `Coordinator` class with `claim_experiment`, `publish_result`, `post_insight`, `publish_hypothesis`, `analyze_swarm` |
| CLI | `ensue create_memory`, `ensue search_memories`, etc. |
| Agent Skill | `npx skills add mutable-state-inc/ensue-skill` |
| Events / Subscriptions | `subscribe_to_memory` — real-time notifications when a memory is updated |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
