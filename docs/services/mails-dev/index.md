---
title: "mails.dev | Agent-Native Services"
service_name: "mails.dev"
description: "Email for AI Agents"
permalink: /services/mails-dev/
page_kind: service
service_slug: "mails-dev"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/mails-dev.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mails-dev.md"
tagline: "Email for AI Agents"
website: "https://mails.dev"
repository: "https://github.com/chekusu/mails"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mails.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/chekusu/mails" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mails-dev.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

mails.dev is **email infrastructure for AI agents** — send and receive emails with a free `@mails.dev` mailbox or your own domain. Agents get programmatic inbox provisioning, full-text search across mail, attachment handling, and a first-class primitive that no human email client needs: **wait for verification code** — `mails code` long-polls until an email with a verification code arrives, then returns it to stdout. This eliminates the agent's need to poll, parse HTML, or guess code patterns.

100 free emails/month on hosted; unlimited with Resend API key or self-hosted Worker.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.
- **Catalog protocols:** URL onboarding, Agent Skill, REST, CLI, SDK, http, API
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ✅ URL Onboarding via skill.md — agent reads https://mails.dev/skill.md and follows instructions
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.

```
Read https://mails.dev/skill.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/mails-dev.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `mails claim`, `mails send`, `mails inbox`, `mails code`, `mails config` |
| REST API | `https://api.mails.dev/v1/send`, `/v1/inbox`, `/v1/code`, `/v1/claim/*` |
| TypeScript SDK | `mails` npm package — `send()`, `getInbox()`, `searchInbox()`, `waitForCode()` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
