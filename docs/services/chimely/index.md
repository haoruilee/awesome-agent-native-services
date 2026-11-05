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
