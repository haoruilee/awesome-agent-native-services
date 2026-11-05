---
title: "OpenMail | Agent-Native Services"
service_name: "OpenMail"
description: "Built for agents, not marketers"
permalink: /services/openmail/
page_kind: service
service_slug: "openmail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/openmail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/openmail.md"
tagline: "Built for agents, not marketers"
website: "https://openmail.sh"
repository: "https://github.com/openmailsh/cli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · websocket · webhook · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openmail.sh" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.openmail.sh" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openmailsh/cli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/openmail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OpenMail is **email infrastructure for AI agents**: one inbox per agent, two-way threading with normal email clients, and inbound delivery over **webhooks or WebSocket** (no polling). Attachments are parsed into **LLM-ready text** (PDFs, CSVs, images, office docs). The product explicitly contrasts itself with newsletter-oriented email APIs.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, websocket, webhook, CLI, http, API
- **MCP:** ⚠️ Not yet published as a first-party MCP server
- **Agent Skill:** ⚠️ No official npx skills add bundle located; openmail setup writes a local skill file with credentials.
- **Onboarding type:** `cli`

## How agents onboard

```bash
npm install -g @openmail/cli
openmail setup
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/openmail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | [API reference](https://docs.openmail.sh/api-reference/introduction) |
| WebSocket | [WebSockets](https://docs.openmail.sh/concepts/websockets) |
| Webhooks | [Webhooks](https://docs.openmail.sh/guides/webhooks) |
| CLI | `@openmail/cli` — `openmail setup` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
