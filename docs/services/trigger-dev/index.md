---
title: "Trigger.dev | Agent-Native Services"
service_name: "Trigger.dev"
description: "Build and deploy fully-managed AI agents and workflows"
permalink: /services/trigger-dev/
page_kind: service
service_slug: "trigger-dev"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/trigger-dev.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/trigger-dev.md"
tagline: "Build and deploy fully-managed AI agents and workflows"
website: "https://trigger.dev"
repository: "https://github.com/triggerdotdev/trigger.dev"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://trigger.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://trigger.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/triggerdotdev/trigger.dev" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/trigger-dev.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Trigger.dev provides a durable execution runtime for AI agent tasks with **no timeouts**, type-safe TypeScript agent definitions, first-class human-in-the-loop pause/resume, full observability, and streaming responses to frontends. Agents can run multi-step workflows for hours or days — surviving infrastructure failures through automatic state checkpointing between steps.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, REST, SDK, API
- **MCP:** ⚠️ No dedicated MCP server published
- **Agent Skill:** ✅ Official skills published at triggerdotdev/skills — see trigger.dev/docs/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | Primary interface — type-safe task definitions, step primitives |
| REST API | Task triggering, status polling, result retrieval |
| Cron | Native `@cron()` decorator for scheduled execution |
| Streaming | Server-sent events for real-time frontend updates |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
