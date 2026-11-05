---
title: "Skyfire | Agent-Native Services"
service_name: "Skyfire"
description: "Identity and payments for autonomous AI agents"
permalink: /services/skyfire/
page_kind: service
service_slug: "skyfire"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/skyfire.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md"
tagline: "Identity and payments for autonomous AI agents"
website: "https://skyfire.xyz"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://skyfire.xyz" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Skyfire is a payment network and identity infrastructure built from the ground up for autonomous AI agents. It provides **Know Your Agent (KYA)** verified identities, agent wallets with programmable spend controls, and an open **KYAPay protocol** — so agents can sign up for services, authenticate, and pay without any human in the transaction loop. Service providers can monetize AI agent access directly, treating agents as a new class of verified customer.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, API
- **MCP:** ⚠️ Not yet publicly documented
- **Agent Skill:** ⚠️ No official skill published by Skyfire yet.
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Wallet management, payment execution, identity operations |
| OAuth2/OIDC | Standard auth protocol extended for agent identity |
| KYAPay Protocol | Open standard for agent checkout — any service can implement receiver side |
| Agent Checkout | Standardized UI/API flow for agent-to-service transactions |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
