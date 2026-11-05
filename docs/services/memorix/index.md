---
title: "Memorix | Agent-Native Services"
service_name: "Memorix"
description: "Local-first shared memory layer for AI coding agents"
permalink: /services/memorix/
page_kind: service
service_slug: "memorix"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memorix.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memorix.md"
tagline: "Local-first shared memory layer for AI coding agents"
verified_at: "2026-10-19"
website: "https://github.com/AVIDS2/memorix"
repository: "https://github.com/AVIDS2/memorix"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Optional</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/AVIDS2/memorix" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/AVIDS2/memorix#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/AVIDS2/memorix" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memorix.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Memorix is a **local-first shared memory daemon anchored to the Git project**. Official README: the agent can change (Claude Code today, Codex tomorrow, Cursor in the afternoon); the project memory stays. SQLite is canonical; Orama searches; LLM formation/embedding is optional — without keys it still does local full-text retrieval.

It is more than a note store: **Git Memory** turns commits into engineering facts; **Reasoning Memory** keeps alternatives and trade-offs; **Memory Autopilot** builds a bounded Workset (`memorix context` / `memorix resume`); **orchestration** (`memorix orchestrate`) coordinates locks, handoffs, and review loops. Long-term curated items cross projects only when explicitly marked portable.

Distinct from [agentmemory](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md) (one memory server, chat/wiki style) and [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md) (per-user observation firehose): Memorix’s identity key is the **git root**, and the surface is a cross-agent local daemon plus setup matrix.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP / memorix setup
- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, STDIO, http
- **MCP:** ✅ Available — stdio is the default; HTTP optional
- **Agent Skill:** ✅ Generated / bundled by memorix setup and memorix skills (not npx skills add)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP / memorix setup

```bash
npm install -g memorix
memorix setup --agent claude --global
# also: codex, copilot, cursor, pi, gemini-cli, opencode, windsurf,
# kiro, antigravity, trae, openclaw, hermes, omp, dsh, workbuddy, …
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memorix.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `memorix setup`, `serve`, `memory`, `orchestrate`, `doctor` |
| MCP stdio | `memorix serve` |
| MCP HTTP | `memorix serve-http` / `background start` |
| SDK | `createMemoryClient()` |
| Dashboard | local web UI (operator, not required) |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/AVIDS2/memorix

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
