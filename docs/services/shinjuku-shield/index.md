---
title: "Shinjuku Shield | Agent-Native Services"
service_name: "Shinjuku Shield"
description: "Privacy-only x402 facilitator for AI agents on Solana"
permalink: /services/shinjuku-shield/
page_kind: service
service_slug: "shinjuku-shield"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/shinjuku-shield.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/shinjuku-shield.md"
tagline: "Privacy-only x402 facilitator for AI agents on Solana"
verified_at: "2026-10-27"
website: "https://shinjukustaition.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Proprietary wallet/binary distribution (SEE LICENSE IN LICENSE.txt on npm shinjuku-shield / shinjuku-shielded); docs/setup repo is public</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://shinjukustaition.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://shinjukustaition.com/llms.txt · https://shinjukustaition.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/shinjuku-shield.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Shinjuku Shield is a **privacy-only x402 facilitator on Solana**. Agents pay any Solana `exact` USDC x402 seller from a **self-custodied shielded balance**; the chain does not show which wallet paid. Sellers keep standard x402 middleware; Shinjuku pays the seller from float after the private agent payment. This is agent payment infrastructure with privacy and local caps — not a generic metered HTTP API behind x402 alone.

---

## Agent-facing interfaces

- **Interaction pattern:** Local self-custody MCP wallet
- **Catalog protocols:** MCP, CLI, STDIO, http
- **MCP:** ✅ Local stdio MCP (agent wallet)
- **Agent Skill:** ⚠️ No official AgentSkills bundle located; primary path is the local MCP wallet via shinjuku setup.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Local self-custody MCP wallet

```bash
npm install -g shinjuku@0.3.86
shinjuku setup
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/shinjuku-shield.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| npm | `shinjuku-shield@0.3.86` / `shinjuku-shielded@0.3.86` / `shinjuku` CLI |
| MCP | stdio after `shinjuku setup` |
| Network | Solana mainnet, USDC |
| Site | https://shinjukustaition.com |

---

## Verification

Last verified **2026-10-27**.

Sources:
- https://shinjukustaition.com

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
