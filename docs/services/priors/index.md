---
title: "Priors | Agent-Native Services"
service_name: "Priors"
description: "Reputation for AI agents that is earned, public and recomputable"
permalink: /services/priors/
page_kind: service
service_slug: "priors"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/priors.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/priors.md"
tagline: "Reputation for AI agents that is earned, public and recomputable"
verified_at: "2026-10-27"
website: "https://priors.trade"
repository: "https://github.com/priors-agents/priors"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://priors.trade" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/priors-agents/priors · https://priors.trade/agent" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/priors-agents/priors" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/priors.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Priors is an **on-chain credit pool for ERC-8004 AI agents** on Robinhood Chain. Agents borrow and repay USDG; every repayment and default is a public event. Score v2 is rebuilt from debt that someone else put at risk. The catalog entry covers the credit/reputation surface and MCP — not generic x402 middleware alone.

---

## Agent-facing interfaces

- **Interaction pattern:** Hosted read-only MCP (no key) + optional SDK/CLI for on-chain actions
- **Catalog protocols:** Agent Skill, MCP, http, API
- **MCP:** ✅ Hosted read-only MCP
- **Agent Skill:** ✅ Official skill folder at skills/priors (plus .claude-plugin). Prefer hosted MCP for read-only score/credit checks.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Hosted read-only MCP (no key) + optional SDK/CLI for on-chain actions

```bash
claude mcp add --transport http priors https://mcp.priors.trade/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/priors.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Hosted MCP | `https://mcp.priors.trade/mcp` |
| npm | `@priors/mcp`, `@priors/x402` |
| HTTP check | `https://priors.trade/api/check?agent=<id>` |
| Chain | Robinhood Chain `eip155:4663` |

---

## Verification

Last verified **2026-10-27**.

Sources:
- https://mcp.priors.trade/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
