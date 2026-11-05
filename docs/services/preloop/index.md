---
title: "Preloop | Agent-Native Services"
service_name: "Preloop"
description: "The Open Source Control Plane for AI Agents"
permalink: /services/preloop/
page_kind: service
service_slug: "preloop"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/preloop.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/preloop.md"
tagline: "The Open Source Control Plane for AI Agents"
verified_at: "2026-09-30"
website: "https://preloop.ai"
repository: "https://github.com/preloop/preloop"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://preloop.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.preloop.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/preloop/preloop" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/preloop.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Preloop is a self-hostable (or Preloop Cloud) control plane for agents that already exist on a machine. It unifies an MCP firewall (allow / deny / require approval / require justification with YAML + CEL), an OpenAI- and Anthropic-compatible model gateway with budgets and attribution, human approvals (mobile, watch, Slack, Mattermost, email, webhook), runtime session timelines, and audit evidence.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI that rewrites local agents onto the control plane
- **Catalog protocols:** MCP, REST, CLI, API
- **MCP:** ✅ Available (firewall / managed MCP)
- **Agent Skill:** ⚠️ Not published as a standard SKILL.md package
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI that rewrites local agents onto the control plane

```bash
curl -fsSL https://preloop.ai/install/cli | sh
preloop signup
# or: preloop login --url http://localhost:3000
preloop agents discover
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/preloop.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `preloop signup`, `login`, `agents discover`, `onboard`, `install-plugin`, `validate` |
| MCP firewall | Managed MCP endpoints after rewrite |
| Model gateway | `/openai/v1/…`, `/anthropic/v1/messages` |
| Control WS | `WS /api/v1/agents/control/ws` |
| REST | Flow execution results, security-screen score, session APIs |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/preloop/preloop/releases/tag/v0.16.0
- https://preloop.ai
- https://docs.preloop.ai

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
