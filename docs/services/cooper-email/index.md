---
title: "Cooper Email | Agent-Native Services"
service_name: "Cooper Email"
description: "HTTP email for autonomous agents"
permalink: /services/cooper-email/
page_kind: service
service_slug: "cooper-email"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/cooper-email.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/cooper-email.md"
tagline: "HTTP email for autonomous agents"
verified_at: "2026-11-15"
website: "https://cooperemail.com"
repository: "https://github.com/cooper-email/cooper-email"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · webhook · CLI · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-15</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cooperemail.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://cooperemail.com/docs.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cooper-email/cooper-email" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/cooper-email.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cooper Email gives each AI agent its own inbox on `cooperemail.com`. One request mints the address and an API key. The agent sends, lists, reads (`extracted_text` with quoted history removed), replies, searches, and long-polls for the next message or a sign-up code. Inbound mail can also arrive as a signed webhook. An optional human owner can approve drafts and recover the account.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, webhook, CLI, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐

```
Read https://cooperemail.com/llms.txt and follow the instructions to create your own email inbox.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/cooper-email.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://cooperemail.com/llms.txt |
| REST API | `https://cooperemail.com/api/v1`, Bearer `coop_live_…` |
| OpenAPI | https://cooperemail.com/openapi.json |
| MCP | `https://cooperemail.com/mcp` |
| Webhooks | Signed `message.received` and the owner wake hook |
| Agent Skills | `npx skills add cooper-email/cooper-email` |
| CLI | https://cooperemail.com/docs/cli |

---

## Verification

Last verified **2026-11-15**.

Sources:
- https://cooperemail.com
- https://cooperemail.com/llms.txt
- https://cooperemail.com/pricing
- https://cooperemail.com/openapi.json
- https://cooperemail.com/mcp
- https://github.com/cooper-email/cooper-email

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
