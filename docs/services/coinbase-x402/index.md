---
title: "Coinbase Developer Platform (x402) | Agent-Native Services"
service_name: "Coinbase Developer Platform (x402)"
description: "HTTP-native payments for the machine web — verify, settle, discover"
permalink: /services/coinbase-x402/
page_kind: service
service_slug: "coinbase-x402"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/coinbase-x402.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/coinbase-x402.md"
tagline: "HTTP-native payments for the machine web — verify, settle, discover"
website: "https://docs.cdp.coinbase.com/x402/welcome"
repository: "https://github.com/coinbase/x402"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.cdp.coinbase.com/x402/welcome" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/coinbase/x402" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/coinbase-x402.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

**x402** revives **HTTP 402 Payment Required** for **machine-to-machine** payments: a client requests a resource, the server responds with payment terms, the client pays (typically stablecoin on EVM or Solana via facilitator), and retries with proof. Coinbase **Developer Platform** provides a **facilitator** (verify/settle), **SDKs**, and **Bazaar** as a discovery layer for x402-enabled endpoints — aimed at **AI agents** and autonomous API consumers paying per call without human checkout.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, http
- **MCP:** ⚠️ Not a standalone MCP product — any MCP agent that performs HTTP can participate in x402 payment flows.
- **Agent Skill:** ⚠️ No official AgentSkills bundle located; integration is SDK + HTTP middleware.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
# Example: Python SDK per coinbase/x402 README
pip install x402
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/coinbase-x402.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP | x402 challenge/response on any compliant host |
| SDKs | https://github.com/coinbase/x402 |
| CDP REST | Facilitator endpoints per [docs](https://docs.cdp.coinbase.com/x402/docs/facilitator) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
