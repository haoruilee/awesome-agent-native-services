---
title: "QM | Agent-Native Services"
service_name: "QM"
description: "A multiplayer agent harness for work. In Slack and on the web"
permalink: /services/qm/
page_kind: service
service_slug: "qm"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/qm.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/qm.md"
tagline: "A multiplayer agent harness for work. In Slack and on the web"
verified_at: "2026-09-26"
website: "https://qm.ycombinator.com"
repository: "https://github.com/yc-software/qm"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT, except where noted upstream</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://qm.ycombinator.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/yc-software/qm/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/yc-software/qm" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/qm.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

QM gives each person and shared room a persistent agent scope with its own memory, files, keychain view, permissions, crons, web apps, skills, and durable sandbox. Personal and shared scopes can collaborate without collapsing their data or authority boundaries. Pi, OpenCode, Codex, and Claude Code can drive the same headless core, so the organization's durable state and policy are not tied to one model vendor.

---

## Agent-facing interfaces

- **Interaction pattern:** Deployment CLI + generated deployment Skill
- **Catalog protocols:** Agent Skill, MCP, CLI, http, API
- **MCP:** ⚠️ Not the primary surface
- **Agent Skill:** ✅ Generated for each deployment
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Deployment CLI + generated deployment Skill

```bash
npm exec --yes --package=@yc-software/qm@latest -- \
  qm init . --org <slug> --target <fly-or-aws>
npm install
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/qm.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP API | Headless core for identity, policy, sessions, and scheduling |
| CLI | `qm init`, validation, deployment, and organization operations |
| Agent harnesses | Pi, OpenCode, Codex, Claude Code adapters |
| Deployment Skill | Generated agent-readable installation and verification workflow |
| Optional channels | Slack service plugin and web/admin/portal plugins |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/yc-software/qm/releases/tag/v0.1.12
- https://qm.ycombinator.com
- https://api.github.com/repos/yc-software/qm

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
