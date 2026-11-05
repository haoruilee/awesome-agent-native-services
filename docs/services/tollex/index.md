---
title: "Tollex | Agent-Native Services"
service_name: "Tollex"
description: "The economic control plane for autonomous software"
permalink: /services/tollex/
page_kind: service
service_slug: "tollex"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/tollex.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/tollex.md"
tagline: "The economic control plane for autonomous software"
website: "https://tollex.org"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · A2A · openapi · json rpc · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://tollex.org" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://tollex.org/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/tollex.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Tollex sells paid capabilities to software agents: Robinhood Chain reads (blocks, logs, balances, `eth_call` simulation), Stock Token prices and halt status, x402 endpoint inspection and receipt verification. An agent states a need and a cost ceiling, gets a free explained plan, pays per call with x402 v2 in USDC on Base or USDG on Robinhood Chain, and receives the result with an EIP-712 signed execution receipt. Uncertain payments are reconciled from the chain, so a lost response never leads to paying twice.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, A2A, openapi, json rpc, http, API
- **MCP:** ⚠️ No hosted MCP endpoint
- **Agent Skill:** ⚠️ Official skill unavailable — its GitHub repository (ShiftAboveCtrl/tollex) returned 404 on 2026-10-13
- **Onboarding type:** `url`

## How agents onboard

```
Read https://tollex.org/llms.txt, then follow https://tollex.org/docs/getting-started/
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/tollex.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP + x402 v2 | `402 PAYMENT-REQUIRED` terms, `PAYMENT-SIGNATURE` payment, `PAYMENT-RESPONSE` settlement and receipt |
| OpenAPI 3.1 | `https://api.tollex.org/openapi.json` with `x-payment-info` per paid route |
| A2A | Agent card at `/.well-known/agent-card.json`, JSON-RPC v1.0 and v0.3, a2a-x402 |
| Discovery | `/.well-known/tollex.json`, `/.well-known/x402`, `llms.txt`; indexed on x402scan |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
