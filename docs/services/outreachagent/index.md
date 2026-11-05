---
title: "OutreachAgent | Agent-Native Services"
service_name: "OutreachAgent"
description: "The Cold Outbound Engine for AI Agents"
permalink: /services/outreachagent/
page_kind: service
service_slug: "outreachagent"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/outreachagent.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/outreachagent.md"
tagline: "The Cold Outbound Engine for AI Agents"
website: "https://outreachagent.dev/"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · REST · webhook · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://outreachagent.dev/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://outreachagent.dev/docs/introduction" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/outreachagent.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OutreachAgent is an API-first outbound email infrastructure platform for teams building AI agents. It lets external agent runtimes create and operate sending identities, compose or manage templates, run multi-step outbound workflows, and route replies or delivery events back into the agent loop.

The service explicitly keeps prospecting, reasoning, copy generation, and next-step decisions in the caller's runtime while it handles inboxes, delivery state, workflows, waits, retries, webhooks, and operational visibility.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, REST, webhook, SDK, openapi, http, API
- **MCP:** ⚠️ Documented, but not currently published to npm.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install @outreachagent/sdk-ts
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/outreachagent.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://api.outreachagent.dev/v1` |
| OpenAPI | https://api.outreachagent.dev/v1/openapi.json |
| TypeScript SDK | `npm install @outreachagent/sdk-ts` |
| MCP | Documented as `@outreachagent/mcp`, but not currently published to npm |
| Webhooks | Signed inbound and workflow event callbacks with retry/replay support |
| LLM context | https://outreachagent.dev/llms-full.txt and https://outreachagent.dev/llms.txt |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
