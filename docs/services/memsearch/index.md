---
title: "MemSearch | Agent-Native Services"
service_name: "MemSearch"
description: "Cross-platform semantic memory for AI coding agents"
permalink: /services/memsearch/
page_kind: service
service_slug: "memsearch"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memsearch.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memsearch.md"
tagline: "Cross-platform semantic memory for AI coding agents"
verified_at: "2026-10-13"
website: "https://zilliztech.github.io/memsearch/"
repository: "https://github.com/zilliztech/memsearch"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://zilliztech.github.io/memsearch/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://zilliztech.github.io/memsearch/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/zilliztech/memsearch" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memsearch.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MemSearch is Zilliz's **search-over-memory** layer for coding agents. Official GitHub description: **"A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus."** Docs: install a plugin and the agent remembers prior work across sessions — conversations are captured, indexed with hybrid search, and recalled when needed.

Markdown under `.memsearch/memory/` is the source of truth. Milvus is a derived, rebuildable index (dense + BM25 + RRF). Recall is progressive: search summaries, expand a section, then drill into the original transcript. The same collection-naming algorithm lets Claude Code, Codex, DeepSeek Harness, OpenClaw, and OpenCode share one project memory.

Official positioning is **retrieval over agent memory**, not a general fact-extraction memory OS. That is the distinction versus Mem0, Zep, and Memoria.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + platform plugins
- **Catalog protocols:** Agent Skill, MCP, CLI, API
- **MCP:** ⚠️ Not the primary published interface.
- **Agent Skill:** ✅ Available as platform skills / SKILL.md recall (not npx skills add).
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + platform plugins

```bash
# CLI / library (ONNX embeddings, no API key)
uv tool install "memsearch[onnx]"

memsearch index ./memory/
memsearch search "how to configure Redis?" --top-k 5
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memsearch.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `memsearch index`, `search`, `expand`, `watch` |
| Python API | `MemSearch(paths=...).index()` / `.search()` |
| Claude Code plugin | Marketplace `zilliztech/memsearch` |
| DSH plugin | `dsh plugin --profile web add @zilliz/memsearch-dsh` |
| OpenClaw | `openclaw plugins install --force clawhub:memsearch` |
| Storage | Markdown + Milvus Lite / Server / Zilliz Cloud |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/zilliztech/memsearch

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
