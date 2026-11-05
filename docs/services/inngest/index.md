---
title: "Inngest | Agent-Native Services"
service_name: "Inngest"
description: "Durable execution for AI agents in production"
permalink: /services/inngest/
page_kind: service
service_slug: "inngest"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/inngest.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inngest.md"
tagline: "Durable execution for AI agents in production"
website: "https://inngest.com"
repository: "https://github.com/inngest/inngest"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://inngest.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.inngest.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/inngest/inngest" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inngest.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Inngest provides a durable execution platform specifically addressing the production challenges of AI agents. It checkpoints state between tool calls, handles external API failures through intelligent retries that preserve agent context, and maps human-in-the-loop approval patterns to native suspend/resume primitives. In 2025, durable execution became a mainstream requirement as AWS, Cloudflare, and Vercel all launched competing offerings — Inngest was ahead of this trend.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, webhook, SDK, API
- **MCP:** ✅ Available (via dev server)
- **Agent Skill:** ✅ Official skills published at inngest/inngest-skills — launched February 2026
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `inngest.createFunction()`, `step.run()`, `step.sleep()`, `step.waitForEvent()` |
| Python SDK | Equivalent Python API |
| REST API | Event triggering, function management |
| Webhooks | External event triggers |
| Cron | Native cron schedule support |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
