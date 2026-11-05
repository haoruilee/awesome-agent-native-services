---
title: "Memoir | Agent-Native Services"
service_name: "Memoir"
description: "Git for AI Memory"
permalink: /services/memoir/
page_kind: service
service_slug: "memoir"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memoir.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoir.md"
tagline: "Git for AI Memory"
verified_at: "2026-10-19"
website: "https://www.memoir-ai.dev"
repository: "https://github.com/zhangfengcdt/memoir"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Alpha — official README badge Status-Alpha; contributing section: “Memoir is alpha”</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.memoir-ai.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://zhangfengcdt.github.io/memoir/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/zhangfengcdt/memoir" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoir.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Memoir replaces opaque vector memory with a **local-first, taxonomy-structured, Git-versioned store**. Official homepage: recall by path (`memoir get api.v2.auth`), time-travel to reproduce bugs, branch to test risky strategies. Claude Code hooks shadow git branches so a `git checkout` does not contaminate `main` memory. Merges review feature-branch lessons into the main knowledge base.

**Alpha:** APIs, plugins, and taxonomy may change. Treat as an early coding-agent memory VCS, not a frozen production SLA.

Distinct from [Memoria](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoria.md) (also git-like, different product) and from [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md) (compressed observation firehose): Memoir’s claim is **hierarchical semantic paths + cryptographic git operations** (`blame` / `checkout` / `merge`), not session-log compression.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / CLI + plugins / MCP
- **Catalog protocols:** Agent Skill, MCP, CLI, SDK
- **MCP:** ✅ Available — memoir-mcp
- **Agent Skill:** ✅ Bundled with Claude Code / Codex plugins (not npx skills add)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / CLI + plugins / MCP

```bash
pip install memoir-ai
# Claude Code:
#   /plugin marketplace add zhangfengcdt/memoir
#   /plugin install memoir@memoir
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoir.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| PyPI | `pip install memoir-ai` (import `memoir`, CLI `memoir`) |
| MCP | `memoir-mcp` via `uvx --from memoir-ai[mcp]` |
| Plugins | Claude Code, Codex, Hermes, OpenClaw, community OpenCode |
| SDK | Async `MemoryClient`; LangGraph `LangGraphMemoryStore` |
| UI | `memoir ui` — local explorer (secondary) |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/zhangfengcdt/memoir

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
