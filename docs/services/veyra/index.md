---
title: "Veyra | Agent-Native Services"
service_name: "Veyra"
description: "Let your AI agents make payments — with guardrails you control"
permalink: /services/veyra/
page_kind: service
service_slug: "veyra"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/veyra.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/veyra.md"
tagline: "Let your AI agents make payments — with guardrails you control"
verified_at: "2026-10-09"
website: "https://veyra.money"
repository: "https://github.com/zapxlabs/veyra-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (veyra-mcp and veyra-examples)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-09</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://veyra.money" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://veyra.money/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/zapxlabs/veyra-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/veyra.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Veyra is a permission layer between an agent and a wallet the owner already controls. The owner sets per-transaction and daily caps and auto / ask / block bands on one MCP endpoint. The agent gets payment tools. It does not get a seed phrase, a private key, or a raw card.

Under the auto-approve limit, with auto-pay enabled, the owner has granted a capped USDC allowance on Base to a relayer Veyra operates. The docs say the token contract enforces that ceiling, and the relayer pays the recipient from the owner's wallet rather than from a Veyra balance. In the ask band the payment returns `awaiting_approval` and a one-time link the owner opens in their own wallet. Over the ask band or the daily cap, the payment is blocked. An approval nobody acts on lapses after 24 hours.

The simulated source settles as `confirmed_simulated` and moves no money. The docs say plain `confirmed` means value moved on-chain. Assets in production are USDC on Base only.

On 2026-10-09 the [pricing page](https://veyra.money/pricing) and [llms.txt](https://veyra.money/llms.txt) both list Free at £0 (1 endpoint, 2 sources, manual approval on every payment, 7-day audit log), Pro at £19/month (up to 10 endpoints and sources, 90-day audit log, auto-pay up to 500 on-chain payments a month), and Team at £79/month (up to 50 endpoints and sources, 1-year audit log with CSV export, auto-pay up to 2,000 on-chain payments a month). Those plan limits are separate from the dollar caps on an endpoint.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP
- **Catalog protocols:** MCP, SDK, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP

```bash
claude mcp add --transport http veyra https://veyra.money/api/mcp \
  --header "Authorization: Bearer veyra_..."
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/veyra.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `POST https://veyra.money/api/mcp` with `Authorization: Bearer veyra_…` |
| stdio | `npx -y veyra-mcp` and `VEYRA_TOKEN` |
| TypeScript SDK | `npm install veyra-mcp` — `VeyraClient` in the same package |
| Registry | `io.github.zapxlabs/veyra` in [server.json](https://github.com/zapxlabs/veyra-mcp/blob/main/server.json) |
| Docs | https://veyra.money/docs and https://veyra.money/llms.txt |

---

## Verification

Last verified **2026-10-09**.

Sources:
- https://veyra.money/api/mcp
- https://veyra.money

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
