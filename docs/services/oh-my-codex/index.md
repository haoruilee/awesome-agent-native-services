---
title: "oh-my-codex (OMX) | Agent-Native Services"
service_name: "oh-my-codex (OMX)"
description: "Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows"
permalink: /services/oh-my-codex/
page_kind: service
service_slug: "oh-my-codex"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/oh-my-codex.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/oh-my-codex.md"
tagline: "Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows"
verified_at: "2026-09-26"
website: "https://oh-my-codex.dev"
repository: "https://github.com/Yeachan-Heo/oh-my-codex"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (root LICENSE file, confirmed 2026-09-26)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Optional</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://oh-my-codex.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Yeachan-Heo/oh-my-codex/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Yeachan-Heo/oh-my-codex" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/oh-my-codex.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OMX keeps Codex as the execution engine and adds a repeatable control layer for planning, durable goals, specialist roles, multi-agent teams, worktree isolation, lifecycle hooks, runtime state, replay, and operator visibility. Its canonical flow moves from clarification and plan review into checkpointed execution, with `.omx/` preserving plans, logs, memory, mission state, worker assignments, and recovery data across turns.

---

## Agent-facing interfaces

- **Interaction pattern:** Codex wrapper CLI + project setup + Agent Skills
- **Catalog protocols:** Agent Skill, MCP, CLI
- **MCP:** ⚠️ Optional compatibility surface
- **Agent Skill:** ✅ Bundled
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Codex wrapper CLI + project setup + Agent Skills

```bash
# Requires an already-working, authenticated Codex CLI and Node.js 20+
codex --version
npm install -g oh-my-codex

# Run from the actual project root
omx setup --scope project --merge-agents
omx doctor
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"

# Safer isolation for an autonomous session
omx --worktree=feat/task --xhigh
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/oh-my-codex.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `omx` setup, launch, exec, doctor, state, team, session, and workflow commands |
| Hooks | Official Codex plugin-scoped hooks plus documented runtime fallbacks |
| Skills | Bundled Codex skills and specialist workflows |
| State/events | Structured JSON/JSONL command, event, snapshot, mission, and checkpoint artifacts |
| Runtime | Codex CLI, tmux/psmux where supported, and Git worktrees |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/Yeachan-Heo/oh-my-codex/releases/tag/v0.21.6
- https://oh-my-codex.dev
- https://api.github.com/repos/Yeachan-Heo/oh-my-codex

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
