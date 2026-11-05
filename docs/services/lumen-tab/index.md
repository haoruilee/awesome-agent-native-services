---
title: "Lumen Tab | Agent-Native Services"
service_name: "Lumen Tab"
description: "Prepaid USDC tabs for pay-per-call AI agent APIs on Arc"
permalink: /services/lumen-tab/
page_kind: service
service_slug: "lumen-tab"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/lumen-tab.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/lumen-tab.md"
tagline: "Prepaid USDC tabs for pay-per-call AI agent APIs on Arc"
verified_at: "2026-10-11"
website: "https://dansgit2b.github.io/lumen-tab/"
repository: "https://github.com/Dansgit2b/lumen-tab"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Early-stage. Days old, 0 stars, not audited, no production users yet. SDK not yet published to npm (install from GitHub). No MCP server or SKILL.md. Start with small deposits.</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-11</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://dansgit2b.github.io/lumen-tab/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Dansgit2b/lumen-tab#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Dansgit2b/lumen-tab" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/lumen-tab.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Lumen Tab is a unidirectional USDC payment channel for pay-per-call HTTP APIs on Arc. An agent opens one prepaid tab with an API provider, then pays each call with a cumulative EIP-712 voucher sent in an `x-lumen-tab` header in reply to an HTTP 402. A paid call needs no transaction and no gas; the provider batch-settles on-chain whenever it wants.

The deposit is a hard spending cap: the provider can never redeem more than the payer signed for, and the payer can exit on its own after the tab's close delay. A tab can name the provider's ERC-8004 agent id.

The project is early-stage: the contract is about 190 lines on OpenZeppelin v5 with 16 Foundry tests and a mainnet demo (3 tabs, 11 paid calls settled in 3 transactions), but it has not been audited and has no production users yet.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK, http
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install github:Dansgit2b/lumen-tab
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/lumen-tab.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Smart contract** | `LumenTab` at `0xb4a0364c58B2DF53e25FfF0463B5434160Ed2B50`, Arc mainnet (chain id 5042) |
| **JS SDK** | viem-based; `signVoucher`, `TabPayer`, `lumenTabPaywall`, `Settler`, `openTab`; install from GitHub (npm publish planned) |
| **HTTP** | HTTP 402 challenge + `x-lumen-tab` voucher header + `x-lumen-tab-receipt` |
| **Dashboard** | Static, read-only page with live tabs, event feed and voucher verifier |
| **MCP** | None |

---

## Verification

Last verified **2026-10-11**.

Sources:
- https://github.com/Dansgit2b/lumen-tab/blob/main/DEPLOYMENTS.md

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
