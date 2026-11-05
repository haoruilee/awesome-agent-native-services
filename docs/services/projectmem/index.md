---
title: "projectmem | Agent-Native Services"
service_name: "projectmem"
description: "We don't make AI smarter. We make it experienced"
permalink: /services/projectmem/
page_kind: service
service_slug: "projectmem"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/projectmem.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/projectmem.md"
tagline: "We don't make AI smarter. We make it experienced"
verified_at: "2026-10-19"
website: "https://www.projectmem.dev"
repository: "https://github.com/riponcm/projectmem"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.projectmem.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.projectmem.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/riponcm/projectmem" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/projectmem.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

projectmem is a **local-first typed event log** plus a **pre-action judgment gate** for coding agents. Memory lives in `.projectmem/` (append-only `events.jsonl`: issues, attempts, fixes, decisions, notes). Git hooks classify commits (`revert` → failed attempt, `fix:` → fix). `pjm precheck` warns *before* a commit if the staged files match a failed approach.

**Judgment, not just recall:** official positioning is “memory + judgment” — stale memories are flagged, never silently deleted; `pjm score` reports a Prevention Score (hours/tokens/dollars). Cross-project gotchas live in `~/.projectmem/global/`. No cloud, no account, no telemetry (optional `--online` update check only).

Distinct from [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md) (session firehose) and [agentmemory](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md) (shared memory server): projectmem’s contract is a **typed development log** and a **pre-commit / pre-action warning**, not chat-memory extraction.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / CLI + MCP
- **Catalog protocols:** MCP, CLI, STDIO
- **MCP:** ✅ Available — native stdio server, 17 tools (homepage); README comparison table also says “15 focused tools”
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / CLI + MCP

```bash
pip install -U projectmem
pjm doctor
pjm doctor --fix
pjm init    # per repo — writes .projectmem/ and git hooks
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/projectmem.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `pjm init`, `doctor`, `precheck`, `wrap`, `score`, `dashboard` |
| MCP | `python -m projectmem.mcp_server` (stdio) |
| Store | `.projectmem/events.jsonl` + distilled markdown |
| Wrap | `pjm wrap claude` / Cursor rules / clipboard |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/riponcm/projectmem

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
