---
title: "Chimely | Agent-Native Services"
service_name: "Chimely"
description: "Open-source, self-hostable in-app notification inbox infrastructure that agents can call through an HTTP API"
permalink: /services/chimely/
page_kind: service
service_slug: "chimely"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/chimely.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/chimely.md"
tagline: "Open-source, self-hostable in-app notification inbox infrastructure that agents can call through an HTTP API"
website: "https://chimely.dev"
repository: "https://github.com/dodopayments/chimely"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0 (server), MIT (SDKs)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">http · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://chimely.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://chimely.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/dodopayments/chimely" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/chimely.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

When a background agent finishes a report, fails a job, or needs someone to approve the next step, the person it works for is usually inside an application, not watching an email client. The natural place to tell them is a notification in that app. Building that from scratch means a notifications table, an API, a real-time channel, and a front-end inbox. Chimely packages those parts. Its own description is "Open-source, self-hostable in-app notification inbox infrastructure that agents can call through an HTTP API."

### Telling the user inside the app

The dossier describes a Rust service backed by Postgres and Redis, with three surfaces. An HTTP API accepts notifications. A Server-Sent-Events hint plane tells connected clients that something new has arrived. A drop-in `<Inbox />` React component renders the inbox in the application. The flow is direct: the agent calls the API, Chimely stores the notification, emits a hint, and the app shows it.

That is the entire agent-facing story, and the dossier says so. Chimely is not a full agent toolkit or a workflow engine. It does not give the agent its own identity; notifications are addressed to end users inside the application, and the agent's authority is whatever API access the application grants it. MCP is not listed. The catalog marks its status as unknown, and the dossier describes the HTTP API as the agent surface. No Agent Skill is published. Any runtime that can make HTTP calls can use it. The [Chimely docs](https://chimely.dev) have the API reference.

The license split matters for some teams: the server is AGPL-3.0 and the SDKs are MIT, per the dossier. Self-hosting is the model, so you run the Rust service, Postgres, and Redis yourself. The dossier positions Chimely as a self-hosted alternative to hosted notification products such as Knock, Courier, MagicBell, and Novu.

### Not an email service

Chimely sits in the [communication collection](/categories/communication/) next to services with a different job. [Agents Mail](/services/agents-mail/), [MailboxKit](/services/mailboxkit/), and [OpenMail](/services/openmail/) give an agent its own email address that can send to and receive from anyone. [MCP Agent Mail](/services/mcp-agent-mail/) is coordination between coding agents. Chimely is one-way from the agent to users of one application, and replies, if any, happen through the app. The [guide to choosing an email API for agents](/guides/choose-an-email-api-for-agents/) is useful mainly to rule email in or out.

Before adopting it, read the docs for how the API authenticates callers, how a notification identifies its recipient, whether read state and deletion are exposed, and how the SSE channel is secured. The record does not cover delivery to email, SMS, or push, and frames that as the point: the agent does not own those channels.

### Editor's take

Choose Chimely if you already run the application your users live in, want agent status and approval prompts to appear there, and are willing to operate the stack under AGPL terms. If the people you need to reach are outside your app, or the agent needs to receive replies, an agent mailbox from Agents Mail or OpenMail is the right category. We formed this view from the dossier and the public docs and repository. None of the stack was deployed or sent a notification for this page.

</section>

## What it does

Chimely is open-source, self-hostable in-app notification inbox infrastructure built with Rust, Postgres, and Redis. It provides an HTTP API, a Server-Sent-Events hint plane, and a drop-in `<Inbox />` React component.

Agents can call Chimely's HTTP notification API to deliver in-app notifications to end users. Chimely is a self-hosted alternative to Knock, Courier, MagicBell, and Novu.

---

## Agent-facing interfaces

- **Catalog protocols:** http, API, documentation
- **MCP:** ⚠️ Not listed
- **Agent Skill:** ⚠️ No dedicated Agent Skills listed
- **Onboarding type:** `documentation`

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP API | Notification API agents can call to deliver in-app notifications |
| Server-Sent Events | Hint plane for notification updates |
| React Component | Drop-in `<Inbox />` component |
| Self-Hosting | Rust + Postgres + Redis |
| Docs | https://chimely.dev |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
