---
title: "MailboxKit | Agent-Native Services"
service_name: "MailboxKit"
description: "Email infrastructure for AI agents"
permalink: /services/mailboxkit/
page_kind: service
service_slug: "mailboxkit"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/mailboxkit.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mailboxkit.md"
tagline: "Email infrastructure for AI agents"
website: "https://mailboxkit.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · webhook · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mailboxkit.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mailboxkit.com/api-docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mailboxkit.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MailboxKit gives **each AI agent a real email address** in seconds: send, receive, and reply through a REST API with **inbound webhooks**, automatic threading (`References` / `In-Reply-To`), optional open/click tracking, and **custom domains** with automated DKIM, SPF, and DMARC. Pricing is pay-as-you-go per email and attachment.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐
- **Catalog protocols:** URL onboarding, Agent Skill, REST, webhook, http, API
- **MCP:** ⚠️ Not yet published as a first-party MCP server
- **Agent Skill:** ✅ URL Onboarding — hosted at https://mailboxkit.com/skill.md
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐

```
Read https://mailboxkit.com/skill.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mailboxkit.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://mailboxkit.com/api/v1` — [API docs](https://mailboxkit.com/api-docs) |
| Webhooks | Inbound email events to HTTPS endpoints |
| URL Onboarding | `https://mailboxkit.com/skill.md` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
