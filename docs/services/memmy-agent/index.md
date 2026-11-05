---
title: "Memmy | Agent-Native Services"
service_name: "Memmy"
description: "Memmy is your personal AI agent & local memory hub for all AI agents — it lets every AI connect to the same memory and keep self-evolving"
permalink: /services/memmy-agent/
page_kind: service
service_slug: "memmy-agent"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memmy-agent.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmy-agent.md"
tagline: "Memmy is your personal AI agent & local memory hub for all AI agents — it lets every AI connect to the same memory and keep self-evolving"
verified_at: "2026-09-26"
website: "https://memmy.bot/"
repository: "https://github.com/MemTensor/memmy-agent"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · REST · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://memmy.bot/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://memmy.bot/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/MemTensor/memmy-agent" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmy-agent.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Memmy provides one local-first memory substrate shared by Codex, Claude Code, Cursor, OpenClaw, Hermes Agent, and other agent surfaces. Hooks, plugins, the desktop app, and the `memmy-memory` CLI all read and write the same SQLite-backed service, so context survives both session restarts and switches between agent products.

Its memory pipeline is more than storage. `turn.start` decides whether and what to recall; parallel vector, full-text, pattern, and structural channels retrieve candidates; fusion, thresholding, deduplication, MMR, and an optional LLM filter select context. `turn.complete` captures a raw turn and L1 traces, while background jobs summarize, reflect, score, embed, and evolve higher-level L2 policies, L3 world models, and callable Skills. The full lifecycle is documented in [How Memory Works](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/overview.mdx).

---

## Agent-facing interfaces

- **Interaction pattern:** local daemon + JSON CLI / REST + installed Agent Skill
- **Catalog protocols:** Agent Skill, REST, CLI, http, API
- **MCP:** ⚠️ No standalone MCP server is documented for the Memory service.
- **Agent Skill:** ✅ Available — bundled with the repository and rendered for supported external agents by Memmy; this is not published as an npx skills add package.
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** local daemon + JSON CLI / REST + installed Agent Skill

```bash
git clone https://github.com/MemTensor/memmy-agent.git && cd memmy-agent
cp .env.example .env
bash scripts/dev-start.sh

memmy-memory init
memmy-memory health
memmy-memory search "memory policies in this project"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmy-agent.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Memory REST API** | Local HTTP at `127.0.0.1:18960`; health, sessions, turns, search/add/get/delete, panel, and analytics endpoints |
| **`memmy-memory` CLI** | JSON output; health, session, turn, search, add/get/delete, config reload, and raw calls |
| **Agent Skills / hooks** | Installs active memory instructions into external agent surfaces and mirrors turns automatically |
| **Agent API** | OpenAI-compatible local API on port `18990` when `memmy serve` runs |
| **Desktop / TUI** | Human management and local Agent Runtime entry points; not required for each memory operation after setup |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/MemTensor/memmy-agent/releases/tag/v1.1.8
- https://memmy.bot/
- https://api.github.com/repos/MemTensor/memmy-agent

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
