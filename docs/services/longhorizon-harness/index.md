---
title: "LongHorizon-Harness | Agent-Native Services"
service_name: "LongHorizon-Harness"
description: "Plan → act → verify → checkpoint or recover → repeat — until the work is actually done"
permalink: /services/longhorizon-harness/
page_kind: service
service_slug: "longhorizon-harness"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/longhorizon-harness.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/longhorizon-harness.md"
tagline: "Plan → act → verify → checkpoint or recover → repeat — until the work is actually done"
verified_at: "2026-09-26"
website: "https://lh-harness.pages.dev"
repository: "https://github.com/AMAP-ML/LongHorizon-Harness"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://lh-harness.pages.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/AMAP-ML/LongHorizon-Harness#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/AMAP-ML/LongHorizon-Harness" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/longhorizon-harness.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

LongHorizon-Harness wraps existing coding and computer-use agents in a repeated Manage–Execute–Audit loop. Every round rebuilds the next bounded step from the original goal, last verified checkpoint, failure evidence, and remaining work. The Executor starts fresh, the Auditor independently checks the real files/UI/logs/tests, and only accepted evidence becomes trusted progress. Run state survives context refreshes and failures.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + agent adapters + optional computer-use plugin
- **Catalog protocols:** MCP, CLI
- **MCP:** ✅ Pass-through configuration
- **Agent Skill:** ⚠️ No standalone published Skill required
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + agent adapters + optional computer-use plugin

```bash
# Python 3.10+; requires Codex or Claude Code on PATH
uv tool install lh-harness

cd /path/to/project
lh-harness init
lh-harness doctor

TASK="Inspect the current directory and summarize its files."
lh-harness run --task "${TASK}" --agent codex
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/longhorizon-harness.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `lh-harness init|doctor|run|web|dashboard|plugin` |
| Configuration | Project `.lh-harness/config.toml` with per-role backend/model and limits |
| Agent adapters | Codex CLI, Claude Code, and custom `AgentAdapter` implementations |
| MCP | Native per-backend config passed into individual runs |
| Artifacts | Structured run state, event stream, role trajectories, audits, and reports |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/AMAP-ML/LongHorizon-Harness/releases/tag/v0.1.7
- https://lh-harness.pages.dev
- https://api.github.com/repos/AMAP-ML/LongHorizon-Harness

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
