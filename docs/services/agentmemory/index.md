---
title: "agentmemory | Agent-Native Services"
service_name: "agentmemory"
description: "Your coding agent remembers everything. No more re-explaining"
permalink: /services/agentmemory/
page_kind: service
service_slug: "agentmemory"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/agentmemory.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md"
tagline: "Your coding agent remembers everything. No more re-explaining"
verified_at: "2026-09-30"
website: "https://agent-memory.dev"
repository: "https://github.com/rohitg00/agentmemory"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agent-memory.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/rohitg00/agentmemory#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/rohitg00/agentmemory" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

agentmemory is a local-first persistent memory layer for coding agents. One memory server is shared across Claude Code, Codex, Cursor, and other MCP clients. It extends an LLM-wiki style store with confidence, lifecycle, knowledge graphs, and hybrid search (built on a pinned iii-engine). Agents save, recall, hand off, and forget through hooks, MCP, REST, and skills instead of re-pasting project lore every session.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ + local memory server + MCP + Skills
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ + local memory server + MCP + Skills

```text
Retrieve and follow the instructions at: https://raw.githubusercontent.com/rohitg00/agentmemory/main/INSTALL_FOR_AGENTS.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `npx @agentmemory/agentmemory`, `agentmemory connect`, `demo` |
| REST | `http://localhost:3111` |
| MCP | `@agentmemory/mcp` stdio |
| Skills | `npx skills add rohitg00/agentmemory -y` |
| Onboarding URL | `INSTALL_FOR_AGENTS.md` |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/rohitg00/agentmemory/releases/tag/v0.9.29

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
