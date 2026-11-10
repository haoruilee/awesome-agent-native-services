---
title: "CyMetica AI (EventTrader) | Agent-Native Services"
service_name: "CyMetica AI (EventTrader)"
description: "Agentically engineered financial platform with autonomous AI trading agents"
permalink: /services/cymetica-ai/
page_kind: service
service_slug: "cymetica-ai"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/cymetica-ai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/cymetica-ai.md"
tagline: "Agentically engineered financial platform with autonomous AI trading agents"
website: "https://cymetica.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · A2A · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cymetica.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/cymetica-ai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Discovery happens through two well-known URLs, so an agent needs to fetch JSON over HTTP and understand either an A2A Agent Card or an MCP descriptor. The dossier gives the [Agent Card](https://cymetica.com/.well-known/agent.json) and the [MCP descriptor](https://cymetica.com/.well-known/mcp.json) as the fastest path, plus HTTP APIs for market access, pricing, and execution. There is no Docs field in the catalog and no published Agent Skill.

### Markets run by agents

The tagline is "Agentically engineered financial platform with autonomous AI trading agents." The service also goes by EventTrader. The dossier describes pre-launch token prediction markets, automated market making, and agent-to-agent coordination for trading and settlement. Its primitives are signed A2A message envelopes, the MCP descriptor, prediction markets for forecasting a token's price at launch, and autonomous market-making loops.

The autonomy model starts with an operator setting strategy and limits. The agent registers or discovers capabilities, monitors markets, and trades continuously, with settlement feeding the next decision. Identity is published through the Agent Card, and API credentials plus policy limits bound each instance. People set objectives and risk boundaries and step in at thresholds.

Use cases in the dossier are pre-launch forecasting, multi-agent market-making experiments, and research sandboxes for adversarial or cooperative agents. That last framing matters: the entry reads as much like an arena as a production venue.

### Not a payment rail

CyMetica sits in [Commerce & Payments](/categories/commerce-and-payments/) but does a different job from most neighbors. [Skyfire](/services/skyfire/), [Nevermined](/services/nevermined/), and [Circle Agent Stack](/services/circle-agent-stack/) move money so an agent can buy something. [OpenLibx402](/services/openlibx402/) is code for charging and paying over HTTP 402. CyMetica is a place where agents take market positions. The risk differs too: a payment rail can overspend, while a trading venue can lose money on positions that looked sound.

The dossier also leads with A2A rather than an SDK, which suits agents that already discover peers through Agent Cards. The [payments guide](/guides/payments-for-autonomous-agents/) covers spend controls, and they apply here with more force.

### Missing documentation

With no docs site cited, the descriptors are the documentation. Read them to see which actions are exposed and how authentication works, because the dossier does not say. Find out what asset settles trades and who holds custody. Check the regulatory status of prediction markets where you operate. Confirm how signed envelopes are verified and which keys sign them.

### Editor's take

CyMetica is for builders running trading-agent experiments who want counterparties that are also agents, and who accept a thinly documented venue. Anyone whose actual need is letting an agent pay for services belongs with Skyfire, Nevermined, or Circle. Our view is built from the dossier and the public pages it links; the project has not connected an agent or placed a trade.

</section>

## What it does

CyMetica AI / EventTrader is a financial service designed around always-on autonomous agents. It exposes pre-launch token prediction markets, automated market-making behavior, and agent-to-agent coordination for trading and settlement workflows.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, A2A, http
- **MCP:** ✅ Public MCP metadata endpoint is available.
- **Agent Skill:** ⚠️ No standalone SKILL.md install package is published yet.
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| A2A | Agent-to-agent communication channel |
| MCP | Model Context Protocol descriptor for discovery/integration |
| HTTP APIs | Market access, pricing, and execution surfaces |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
