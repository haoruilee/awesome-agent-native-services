---
title: "Agentuity | Agent-Native Services"
service_name: "Agentuity"
description: "The Full-Stack Platform for AI Agents"
permalink: /services/agentuity/
page_kind: service
service_slug: "agentuity"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/agentuity.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentuity.md"
tagline: "The Full-Stack Platform for AI Agents"
website: "https://agentuity.com"
repository: "https://github.com/agentuity/sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">webhook · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentuity.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentcompany.com/agentuity" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentuity/sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentuity.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agentuity is a deployment and runtime platform for **AI agents as workloads**: type-safe APIs and optional React frontends, **Postgres / Redis / vector / object storage** exposed to agents as tools, **ephemeral sandboxes** for untrusted code, **OpenTelemetry**-based observability (prompts, responses, cost per span), **evals** tied to production traffic, and **I/O** integrations (email, SMS, webhooks, cron). It targets **long-running, session-oriented agent execution** rather than classic stateless HTTP services — see [AI agent infrastructure](https://agentuity.com/ai-agent-infrastructure) and related architecture guides on the marketing site.

---

## Agent-facing interfaces

- **Catalog protocols:** webhook, CLI, SDK, http, API
- **MCP:** ⚠️ No dedicated MCP server documented as a first-class product surface.
- **Agent Skill:** ⚠️ No official SKILL.md registry entry located yet.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
# Follow quickstart at https://agentcompany.com/agentuity — install CLI and SDK, then deploy.
# Example pattern (see official docs for current commands):
npm install @agentuity/sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agentuity.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `@agentuity/sdk` — see GitHub |
| Python SDK | `agentuity` — see GitHub |
| CLI | `agentuity` CLI — see GitHub |
| HTTP / Webhooks | Product I/O and API routes — see https://agentcompany.com/agentuity |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
