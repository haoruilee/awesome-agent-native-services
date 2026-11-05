---
title: "Engram | Agent-Native Services"
service_name: "Engram"
description: "Persistent memory for AI coding agents"
permalink: /services/engram/
page_kind: service
service_slug: "engram"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/engram.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/engram.md"
tagline: "Persistent memory for AI coding agents"
verified_at: "2026-10-13"
website: "https://engram.gentlemanprogramming.com/"
repository: "https://github.com/Gentleman-Programming/engram"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://engram.gentlemanprogramming.com/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://engram.gentlemanprogramming.com/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Gentleman-Programming/engram" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/engram.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Engram is a **single Go binary** that gives coding agents a persistent SQLite + FTS5 memory. Official positioning: the **agent** decides what is worth remembering via `mem_save`; Engram stores and searches it. Docs: "Engram trusts the agent to decide what's worth remembering — not a firehose of raw tool calls."

Next session, the agent calls `mem_search` / `mem_context` (and plugins can inject prior session context). Progressive disclosure is `mem_search` → `mem_timeline` → `mem_get_observation`. Optional git-chunk sync and opt-in cloud replication leave local SQLite authoritative.

**Distinct from [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md):** Claude-Mem auto-captures a tool-call firehose and compresses it in a worker. Engram is agent-curated FTS5 — one binary, zero Node/Bun/Python/Chroma. Their [COMPARISON.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/COMPARISON.md) is the official contrast (note: that file's Claude-Mem **AGPL-3.0** license row is stale; Claude-Mem relicensed to Apache-2.0 in v13.0.0).

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP / plugin
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available — stdio MCP is the primary agent surface.
- **Agent Skill:** ✅ Published as a Claude Code marketplace plugin with a Memory Protocol skill (not npx skills add).
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP / plugin

```bash
brew install gentleman-programming/tap/engram
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/engram.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Homebrew | `brew install gentleman-programming/tap/engram` |
| Agent setup | `engram setup <codex\|opencode\|cursor\|…>` or Claude Code marketplace plugin |
| MCP stdio | `engram mcp` |
| HTTP API | `engram serve` (default 7437) — not an MCP transport |
| CLI | `engram save`, `search`, `timeline`, `context`, `sync`, `doctor`, … |
| TUI | `engram tui` |
| Docs | https://engram.gentlemanprogramming.com/ |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/Gentleman-Programming/engram

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
