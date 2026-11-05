---
title: "AgenticMail | Agent-Native Services"
service_name: "AgenticMail"
description: "Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically"
permalink: /services/agenticmail/
page_kind: service
service_slug: "agenticmail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agenticmail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agenticmail.md"
tagline: "Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically"
website: "https://github.com/agenticmail/agenticmail"
repository: "https://github.com/agenticmail/agenticmail"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open source · self-hosted · v0.5.x (rapid iteration through 2026)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · webhook · CLI · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/agenticmail/agenticmail" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/agenticmail/agenticmail#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agenticmail/agenticmail" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agenticmail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgenticMail is a self-hosted platform that gives every AI agent a **real email address and a real phone number** — not a forwarder, not an alias on top of a human account, but a stand-alone communication identity owned by the agent. It bundles a local Stalwart mail server (run via Docker), an inbound webhook system, an SMS/voice integration that proxies to Google Voice, and a REST surface of 75+ endpoints covering inboxes, threads, attachments, contacts, message search, and outbound delivery.

The design choice that distinguishes it from existing entries in this category is the unified email + SMS identity: one provisioning call yields both an `@<your-domain>` mailbox and a programmable phone number, so agents can complete sign-ups that require either form of 2FA without dropping into a different vendor.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, webhook, CLI, API
- **MCP:** ⚠️ Not yet published as a first-party MCP server. The 75+ REST endpoints are designed to be wrapped by any MCP host (Claude Code, Cursor, Gemini CLI). Community wrappers are in progress.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `cli`

## How agents onboard

```
# Self-hosted (Docker):
git clone https://github.com/agenticmail/agenticmail
cd agenticmail && docker compose up -d
# then: POST /api/v1/inboxes  →  receive an @<your-domain> address
# and:  POST /api/v1/sms      →  send/receive SMS via Google Voice
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agenticmail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | 75+ endpoints (inboxes, threads, messages, SMS, contacts, search) |
| Webhooks | Inbound mail + SMS push |
| Self-hosted SMTP/IMAP | Stalwart mail server runs in-cluster |
| SMS/Voice Bridge | Google Voice integration for programmable phone numbers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
