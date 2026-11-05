---
title: "Beads | Agent-Native Services"
service_name: "Beads"
description: "Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss"
permalink: /services/beads/
page_kind: service
service_slug: "beads"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/beads.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/beads.md"
tagline: "Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss"
verified_at: "2026-10-19"
website: "https://beads.gascity.com"
repository: "https://github.com/gastownhall/beads"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Optional</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://beads.gascity.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://beads.gascity.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/gastownhall/beads" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/beads.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Beads (`bd`) is a **dependency-aware work graph** for coding agents, stored in a [Dolt](https://github.com/dolthub/dolt) version-controlled SQL database. Official docs: traditional trackers were not designed for agents; Beads uses hash IDs (`bd-a1b2`) so concurrent agents do not collide, `bd ready` so an agent only claims unblocked work, and Dolt push/pull so the graph survives context loss across machines.

This is **not fact memory**. Distinct from [agentmemory](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md) (shared memory server), and [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md) (tool-call firehose + compression): Beads tracks issues, blockers, formulas/molecules, and `bd remember` project insights as a **work graph**, not a fact/RAG store.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + optional MCP / agent setup recipes
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available — optional; the primary surface is the bd CLI
- **Agent Skill:** ✅ Bundled with bd setup (not npx skills add)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + optional MCP / agent setup recipes

```bash
brew install beads
# or: curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash
# or: npm install -g @beads/bd

cd your-project
bd init --quiet
bd setup claude    # also: codex, cursor, factory, mux, gemini, copilot, …
bd ready --json
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/beads.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `bd` — `--json` on list/show/create |
| MCP | `beads-mcp` stdio |
| Agent setup | `bd setup claude\|codex\|cursor\|…` |
| Sync | `bd dolt push` / `bd dolt pull` |
| Docs | https://beads.gascity.com — also `/llms.txt` index |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/gastownhall/beads

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
