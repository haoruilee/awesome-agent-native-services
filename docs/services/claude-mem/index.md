---
title: "Claude-Mem | Agent-Native Services"
service_name: "Claude-Mem"
description: "Persistent memory compression system for Claude Code"
permalink: /services/claude-mem/
page_kind: service
service_slug: "claude-mem"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/claude-mem.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md"
tagline: "Persistent memory compression system for Claude Code"
verified_at: "2026-10-13"
website: "https://cmem.ai/"
repository: "https://github.com/thedotmack/claude-mem"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (relicensed from AGPL-3.0 in v13.0.0, 2026-05-08)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cmem.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.claude-mem.ai/introduction" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/thedotmack/claude-mem" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Claude-Mem is a **persistent memory compression system** for coding agents. Official docs: it automatically captures tool-usage observations, generates semantic summaries, and injects relevant context into later sessions so the agent keeps project continuity after a session ends.

The capture path is a **firehose**: lifecycle hooks record prompts and tool executions (Read, Write, and the rest), a local Bun worker compresses them via the Claude Agent SDK, and the next SessionStart primes context from recent sessions. Storage is SQLite + FTS5 with an optional Chroma vector index.

**Distinct from [MemPalace](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md)** (verbatim palace rooms/drawers, no official paraphrase) and **[MemSearch](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memsearch.md)** (Markdown + Milvus hybrid search plugins): Claude-Mem auto-captures a tool-call firehose, compresses it, and primes the next session.

**OSS vs hosted:** Apache-2.0 covers the local engine, CLI, MCP tools, and docs. [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md) states Claude-Mem Server v0.1 does **not** ship hosted cloud, team sync, enterprise features, premium knowledge agents, private evals, or customer deployment tooling — those sit outside the public implementation. CMEM Cloud (homepage: paid cloud mirror + private MCP link) is that hosted layer.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + coding-agent plugin
- **Catalog protocols:** Agent Skill, MCP, CLI, http, API
- **MCP:** ✅ Available — four search tools on the local worker.
- **Agent Skill:** ✅ Bundled with the plugin (not npx skills add).
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + coding-agent plugin

```bash
npx claude-mem install
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Installer | `npx claude-mem install` (multi-IDE) |
| Claude Code plugin | `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem` |
| OpenCode / Antigravity | `npx claude-mem install --ide opencode` / `--ide antigravity` |
| OpenClaw | `curl -fsSL https://install.cmem.ai/openclaw.sh \| bash` |
| MCP search | `search`, `timeline`, `get_observations` |
| Worker HTTP | Local API + web viewer (port printed on startup) |
| Docs | https://docs.claude-mem.ai/introduction |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/thedotmack/claude-mem

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
