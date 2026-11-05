---
title: "AgentsPay | Agent-Native Services"
service_name: "AgentsPay"
description: "Crypto identity and embedded wallets for AI agents"
permalink: /services/agentspay/
page_kind: service
service_slug: "agentspay"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/agentspay.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md"
tagline: "Crypto identity and embedded wallets for AI agents"
website: "https://agentspay.dev"
repository: "https://github.com/AgentPayy/agentpayy-platform"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentspay.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/AgentPayy/agentpayy-platform" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentsPay issues **W3C Decentralized Identifiers (DIDs)** to AI agents on the Base L2 blockchain, embeds USDC wallets with operator-set spending limits, and provides an MCP-native API gateway. Agents can discover which services require payment and pay for them directly — solving the common agent failure mode where execution halts when an API key or payment is needed.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, API
- **MCP:** ✅ MCP-Native
- **Agent Skill:** ⚠️ No official skill published by AgentsPay yet.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| MCP-Native API Gateway | Primary interface for service discovery and payment |
| REST API | Wallet management, DID operations |
| Base L2 | On-chain identity and transaction recording |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
