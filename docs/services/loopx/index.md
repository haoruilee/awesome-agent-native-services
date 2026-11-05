---
title: "LoopX | Agent-Native Services"
service_name: "LoopX"
description: "The open, provider-neutral, stateful control plane for long-horizon agents"
permalink: /services/loopx/
page_kind: service
service_slug: "loopx"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/loopx.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/loopx.md"
tagline: "The open, provider-neutral, stateful control plane for long-horizon agents"
verified_at: "2026-09-30"
website: "https://loopx-project.github.io/loopx/"
repository: "https://github.com/loopx-project/loopx"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://loopx-project.github.io/loopx/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://loopx-project.github.io/loopx/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/loopx-project/loopx" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/loopx.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

LoopX is a provider-neutral control plane for work that outlives one chat turn. It keeps objectives, gates, todos, evidence, quota, and handoffs while Codex, Claude Code, Cursor, or another harness executes a bounded slice. Registered agents are peers that claim leases; humans keep dangerous permissions and final ownership. Official text: it is not an autonomous production controller.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + workflow skills
- **Catalog protocols:** Agent Skill, MCP, CLI
- **MCP:** ⚠️ Not the primary surface
- **Agent Skill:** ✅ Available (installer-registered workflow skills)
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + workflow skills

```bash
python3 -m pip install --upgrade loopx
loopx workflow-skills --install
loopx doctor
cd /path/to/your-project
loopx connect
loopx status
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/loopx.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `loopx connect`, `doctor`, `status`, `start-goal`, `workflow-skills` |
| Skills | Host-registered LoopX command/workflow skills |
| State | `.loopx/`, goal-state markdown |
| Host adapters | Codex App, Claude Code, OpenCode, Pi, KunlunCode, Cursor/shell |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/loopx-project/loopx/releases/tag/v1.2.3
- https://loopx-project.github.io/loopx/
- https://loopx-project.github.io/loopx/docs/

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
