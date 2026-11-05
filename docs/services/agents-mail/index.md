---
title: "Agents Mail | Agent-Native Services"
service_name: "Agents Mail"
description: "Email for AI Agents"
permalink: /services/agents-mail/
page_kind: service
service_slug: "agents-mail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agents-mail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md"
tagline: "Email for AI Agents"
website: "https://agentsmail.org"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentsmail.org" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentsmail.org/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agents Mail provides mailbox infrastructure specifically for AI agents: programmatic inbox creation, sending/replying to email, message retrieval, and machine-readable onboarding/discovery metadata. The service is explicitly framed as communication infrastructure for autonomous agents rather than as a human mailbox product with add-on APIs.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, http, API
- **MCP:** ⚠️ Not yet published as an official dedicated MCP server (as of April 15, 2026).
- **Agent Skill:** ✅ Available (URL onboarding)
- **Onboarding type:** `url`

## How agents onboard

```text
https://agentsmail.org/skill.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | https://agentsmail.org/docs |
| URL onboarding | `https://agentsmail.org/skill.md` |
| Agent metadata | `https://agentsmail.org/.well-known/agent.json` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
