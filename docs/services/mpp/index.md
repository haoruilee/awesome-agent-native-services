---
title: "MPP | Agent-Native Services"
service_name: "MPP"
description: "MPP lets agents pay for services on the web, extensible to any payment method"
permalink: /services/mpp/
page_kind: service
service_slug: "mpp"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/mpp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/mpp.md"
tagline: "MPP lets agents pay for services on the web, extensible to any payment method"
verified_at: "2026-10-13"
website: "https://mpp.dev"
repository: "https://github.com/wevm/mppx"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (wevm/mppx); protocol/site repos are separate (see Official Repo)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mpp.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mpp.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/wevm/mppx" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/mpp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MPP (Machine Payments Protocol) is an open **pay-in-the-request** standard. Official `llms.txt`: it standardizes HTTP 402 for machine-to-machine payments. Flow: **Challenge → Credential → Receipt**. A server answers `402 Payment Required` with accepted methods and price; the client pays (Tempo stablecoins, cards/Stripe, Lightning, EVM, and other documented rails) and retries; the server returns a `Payment-Receipt`.

It is designed so agents do not need pre-provisioned API keys or a checkout form ([agentic payments](https://mpp.dev/use-cases/agentic-payments)). Sessions support metered pay-as-you-go (including per-token). `mppx` is the TypeScript interface: client polyfill, server `charge`, CLI, and a payments `Proxy`.

**Distinct from catalog x402 / [OpenLibx402](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/openlibx402.md):** those are the IETF-adjacent HTTP 402 / `PAYMENT-REQUIRED` crypto rail. MPP adds cards, bank-style Stripe paths, Lightning, Tempo sessions, and can *also* speak x402 exact from one SDK. **Distinct from [AP2](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ap2.md) / [UCP](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ucp.md):** those are checkout mandates and a commerce language, not inline HTTP 402. **Distinct from [Skyfire](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md) / [AgentsPay](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md) / [Circle Agent Stack](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/circle-agent-stack.md) / [Payman AI](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/payman-ai.md):** hosted KYA/wallets, not an open pay-in-the-request protocol.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + HTTP 402
- **Catalog protocols:** MCP, CLI, SDK, http, API
- **MCP:** ✅ First-class transport and SDK, not a single hosted "MPP MCP server."
- **Agent Skill:** ⚠️ No official npx skills add package. Docs ship copy-paste prompt mode for agents.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK + HTTP 402

```bash
npm i mppx
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/mpp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Spec / site | https://mpp.dev — site source [tempoxyz/mpp](https://github.com/tempoxyz/mpp) |
| Protocol drafts | [tempoxyz/mpp-specs](https://github.com/tempoxyz/mpp-specs) — Payment HTTP auth scheme |
| TypeScript SDK | `npm i mppx` — [wevm/mppx](https://github.com/wevm/mppx) |
| CLI | `npx mppx account create` then `mppx example.com` |
| MCP | Client wrap + server `Transport.mcpSdk()` |
| Docs MCP | `https://mpp.dev/api/mcp` |
| x402 interop | Same `mppx` fetch can satisfy x402 exact |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/wevm/mppx

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
