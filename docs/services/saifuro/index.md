---
title: "Saifuro | Agent-Native Services"
service_name: "Saifuro"
description: "The financial OS for the AI agent economy"
permalink: /services/saifuro/
page_kind: service
service_slug: "saifuro"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/saifuro.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/saifuro.md"
tagline: "The financial OS for the AI agent economy"
verified_at: "2026-10-05"
website: "https://saifuro.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Closed access. Keys are issued per organization at onboarding; there is no public sandbox signup, because the product authorizes spending on behalf of a paying organization. Escrow is simulated in the sandbox. Documented gaps are maintained by the vendor at Known gaps</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · webhook · CLI · ACP · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-05</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://saifuro.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.saifuro.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/saifuro.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Saifuro is an authorization layer that sits between an organization's agents and its payment providers. The operator writes a mandate per agent — who the agent acts for, how much it may spend per transaction and per month, in which categories, above which amount a human must approve, and when the mandate expires. Every spend request is evaluated against that mandate synchronously, before money moves, and the answer is one of eight decision codes carried in a signed token.

The signature is the part that makes this usable between two parties that do not share a backend. A verdict is an ES256 JWT bound to the request that produced it — amount, recipient, mandate, policy version and a nonce are covered by the signature — so a seller's agent can verify that the buyer's agent was actually authorized for this amount, offline, against a public JWKS, without an account and without taking the buyer's word for it. Every decision, whatever the verdict, lands in an append-only log that exports as NDJSON.

Saifuro is deliberately not in the money path: it holds no customer funds, takes no custody, and routes settlement through the customer's own licensed providers. For conditional agent-to-agent deals it deploys escrow contracts on Base and Solana settling in USDC, where the funds sit in the contract rather than with Saifuro — in the sandbox those escrows are simulated rather than deployed.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, webhook, CLI, ACP, API
- **MCP:** ⚠️ No first-party MCP server is documented. The verified agent surface is the versioned REST API plus webhooks; the private TypeScript SDK wraps the same endpoints.
- **Agent Skill:** ⚠️ Not yet published by the vendor.
- **Onboarding type:** `cli`

## How agents onboard

```bash
curl -s https://api.saifuro.com/v1/authorizations \
  -H "Authorization: Bearer $SAIFURO_AGENT_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "amount": 120.00, "currency": "USD", "recipient": "vendor:acme_saas", "category": "saas" }'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/saifuro.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `api.saifuro.com`, versioned; `/v1/authorizations`, `/v1/mandates`, `/v1/agents`, `/v1/decisions`, `/v1/escrows`, `/v1/reviews/{id}/approve`, `/v1/enforcement`, `/v1/usage`, `/v1/exports`, `/v1/webhooks` |
| Verdict verification | ES256 JWS verified against https://verdicts.saifuro.com/.well-known/jwks.json — no account required |
| Webhooks | Per state change, including `escrow.funded`, `escrow.released`, `escrow.refunded` and review events |
| Exports | NDJSON decision stream, one record per evaluated request, including the `verdict_token` |
| SDK | Private TypeScript SDK issued at onboarding; the npm package name is a reservation, not a published library |
| MCP | ⚠️ None documented |
| Payment rails | Positioned as one integration across x402, MPP, ACP, AP2 and the card agent programs, with settlement executed by the customer's licensed providers |

---

## Verification

Last verified **2026-10-05**.

Sources:
- https://saifuro.com

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
