---
title: "TencentDB Agent Memory | Agent-Native Services"
service_name: "TencentDB Agent Memory"
description: "Agents remember,Humans innovate"
permalink: /services/tencentdb-agent-memory/
page_kind: service
service_slug: "tencentdb-agent-memory"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/tencentdb-agent-memory.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/tencentdb-agent-memory.md"
tagline: "Agents remember,Humans innovate"
verified_at: "2026-09-30"
website: "https://github.com/TencentCloud/TencentDB-Agent-Memory"
repository: "https://github.com/TencentCloud/TencentDB-Agent-Memory"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (LICENSE file; GitHub SPDX shows NOASSERTION)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/tencentdb-agent-memory.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

TencentDB Agent Memory is a layered memory system for long-horizon agents. Short-term memory offloads verbose tool logs and keeps a compact Mermaid symbol graph with `node_id` drill-down to raw `refs/*.md`. Long-term memory builds L0 conversation → L1 atoms → L2 scenarios → L3 persona instead of a flat vector pile. GitHub description also frames a team hub of Chat Memory, Skill, LLM-Wiki, and Code-Graph assets. Official README quotes relative OpenClaw benchmark deltas (WideSearch, SWE-bench, AA-LCR, PersonaMem); treat those as upstream-reported, not independently re-measured here.

---

## Agent-facing interfaces

- **Interaction pattern:** OpenClaw plugin or Hermes gateway plugin
- **Catalog protocols:** http
- **MCP:** ⚠️ Not published as a standalone MCP server
- **Agent Skill:** ⚠️ Not published as npx skills add
- **Onboarding type:** `other`

## How agents onboard

**Interaction pattern:** OpenClaw plugin or Hermes gateway plugin

```bash
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb
openclaw gateway restart
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/tencentdb-agent-memory.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| npm plugin | `@tencentdb-agent-memory/memory-tencentdb` |
| OpenClaw | `openclaw plugins install …` |
| Hermes Gateway | HTTP capture/search/recall (example `:8420`) |
| Local store | SQLite + sqlite-vec by default |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/TencentCloud/TencentDB-Agent-Memory/releases/tag/v2.0.1

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
