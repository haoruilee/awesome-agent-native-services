---
title: "Universal Commerce Protocol (UCP) | Agent-Native Services"
service_name: "Universal Commerce Protocol (UCP)"
description: "The common language for platforms, agents, and businesses"
permalink: /services/ucp/
page_kind: service
service_slug: "ucp"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/ucp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ucp.md"
tagline: "The common language for platforms, agents, and businesses"
verified_at: "2026-10-13"
website: "https://ucp.dev"
repository: "https://github.com/Universal-Commerce-Protocol/ucp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · SDK · A2A · json rpc · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://ucp.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://ucp.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Universal-Commerce-Protocol/ucp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ucp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

The Universal Commerce Protocol is an open standard for **agentic commerce**: discovery, cart, identity linking, checkout, and order lifecycle across shopping (and, the homepage says, expanding into lodging and food). Official homepage copy: UCP provides building blocks so platforms, agents, and businesses share one standard instead of custom builds.

Capabilities are modular (Checkout, Identity Linking, Order, Payment Token Exchange) with extensions (discounts, fulfillment). Businesses publish a profile of supported capabilities so platforms can discover them autonomously. Checkout sessions can run with or without a human present. Payments use existing rails plus AP2 mandates and verifiable credentials rather than inventing a new wallet.

This is distinct from catalog x402, Skyfire, and Circle: those are payment/wallet or HTTP-402 settlement layers. UCP is the **checkout and commerce protocol** those rails can plug into.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + protocol spec
- **Catalog protocols:** MCP, REST, CLI, SDK, A2A, json rpc, http
- **MCP:** ✅ Documented as a first-class transport — UCP is transport-agnostic.
- **Agent Skill:** ⚠️ No official Agent Skills package published.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK + protocol spec

```bash
# Schema tool agents use to resolve ucp_* annotations at runtime
cargo install ucp-schema

# Spec + docs checkout
git clone https://github.com/Universal-Commerce-Protocol/ucp.git
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ucp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Spec / docs | https://ucp.dev and this repository's `source/` schemas |
| REST / JSON-RPC | Documented transports |
| MCP / A2A | Built-in support for agent frameworks |
| Schema CLI | `cargo install ucp-schema` |
| Samples / SDKs / conformance | Sister repos under [Universal-Commerce-Protocol](https://github.com/Universal-Commerce-Protocol) |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/Universal-Commerce-Protocol/ucp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
