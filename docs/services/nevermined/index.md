---
title: "Nevermined | Agent-Native Services"
service_name: "Nevermined"
description: "The payment layer AI agents actually need"
permalink: /services/nevermined/
page_kind: service
service_slug: "nevermined"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/nevermined.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/nevermined.md"
tagline: "The payment layer AI agents actually need"
website: "https://nevermined.ai/"
repository: "https://github.com/nevermined-io/payments"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://nevermined.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/nevermined-io/payments" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/nevermined.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Nevermined's **x402 Facilitator** embeds payment directly into the HTTP protocol. When an agent makes an API request, the server responds with HTTP 402 Payment Required; the agent pays via the x402 protocol and the request is fulfilled — all within a single HTTP exchange. No human checkout flow. No redirect. Payment is part of the API call itself.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, http, API
- **MCP:** ⚠️ Not yet published as standalone MCP server
- **Agent Skill:** ⚠️ No official skill published by Nevermined yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP x402 | Standard 402 response with payment terms; agent-side Facilitator handles payment |
| REST API | Account management, budget configuration, transaction history |
| Payment Methods | Fiat, crypto, stablecoins (USDC), prepaid credits |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
