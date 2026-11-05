---
title: "send21 | Agent-Native Services"
service_name: "send21"
description: "Payments for AI agents, without giving them your keys"
permalink: /services/send21/
page_kind: service
service_slug: "send21"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/send21.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/send21.md"
tagline: "Payments for AI agents, without giving them your keys"
verified_at: "2026-10-27"
website: "https://send21.io"
repository: "https://github.com/send21io/send21-examples"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · webhook · SDK · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://send21.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://send21.io/docs/mcp" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/send21io/send21-examples" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/send21.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

send21 is non-custodial payment software for crypto pay links and payment drafts. An agent creates a payment request (a pay link that offers several currencies) or a draft (one payment to one receiver), priced in a crypto amount or in any of 161 fiat currencies with an exchange rate locked for 15 minutes. send21 watches the chain and reports progress by status endpoint and signed webhook until the payment confirms.

The payment itself is signed in a wallet the agent does not control: the payer's own wallet, or the operator's wallet through a transaction template. Assets per network: BTC on Bitcoin and Lightning; USDC, USDT, EURC, SOL and wrapped BTC on Solana; USDC, USDT, EURC, ETH and WBTC on Ethereum; USDC, EURC and ETH on Base; native USDC and ETH on Arbitrum; native USDC on Polygon.

People use the same product through the web app. The agent surface (scoped keys, MCP, idempotent create and track) is what this entry covers.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP
- **Catalog protocols:** Agent Skill, MCP, REST, webhook, SDK, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP

```bash
claude mcp add --transport http send21 https://send21.io/mcp \
  --header "Authorization: Bearer s21_..."
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/send21.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `Authorization: Bearer s21_...`; OpenAPI at https://send21.io/openapi.json; 300 requests per minute per key |
| MCP | `https://send21.io/mcp` (Streamable HTTP, stateless) and `https://send21.io/mcp/oauth` |
| Webhooks | `POST /api/v1/webhooks`; HMAC-SHA256 signatures, up to 8 attempts — [docs](https://send21.io/docs/webhooks) |
| Python | `pip install langchain-send21` |
| TypeScript | `npm install ai-sdk-tool-send21 ai zod` (Vercel AI SDK) |
| Docs | https://send21.io/llms.txt and https://send21.io/llms-full.txt |

---

## Verification

Last verified **2026-10-27**.

Sources:
- https://send21.io/mcp
- https://send21.io/llms-full.txt

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
