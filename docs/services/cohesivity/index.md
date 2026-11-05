---
title: "Cohesivity | Agent-Native Services"
service_name: "Cohesivity"
description: "backend infra your agents can actually use"
permalink: /services/cohesivity/
page_kind: service
service_slug: "cohesivity"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cohesivity.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cohesivity.md"
tagline: "backend infra your agents can actually use"
website: "https://cohesivity.ai"
repository: "https://github.com/cohesivity-org/cohesivity-plugin"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cohesivity.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://cohesivity.ai/llms.txt · https://cohesivity.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cohesivity-org/cohesivity-plugin" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cohesivity.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cohesivity is on-the-fly backend infrastructure for coding agents: one managed API for a project's databases, auth, hosting, storage, inbox, browser sessions, and AI/search APIs. The agent provisions an ephemeral project tenant without separate vendor accounts. Provider keys stay server-side; the app calls Cohesivity's edge. Humans claim the tenant if they want to keep it past 72 hours.

**Dual-use honesty:** Postgres, object storage, and similar offerings are ordinary application primitives. This listing covers the agent-facing tenant bootstrap, inbox, MCP/skill surface, and consent model — not a claim that every endpoint is exclusively agent-specific.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI
- **Catalog protocols:** Agent Skill, MCP, STDIO, http, API
- **MCP:** ✅ Available — two different servers
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** CLI

```bash
npx --yes @cohesivity/init@0.8.3
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cohesivity.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Homepage | https://cohesivity.ai |
| Agent docs | https://cohesivity.ai/llms.txt · https://cohesivity.ai/llms-full.txt · https://cohesivity.ai/skill.md |
| Management API | `https://cohesivity.ai/api/*` with `Authorization: Bearer <coh_management_key>` |
| Edge / data plane | `https://cohesivity.ai/edge/*` with application key (server-side only) |
| Docs MCP | https://cohesivity.ai/mcp — read-only |
| Mutating MCP | Plugin local stdio; https://cohesivity.ai/mcp/manage |
| Installer | `npx --yes @cohesivity/init@0.8.3` |
| Plugin | https://github.com/cohesivity-org/cohesivity-plugin |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
