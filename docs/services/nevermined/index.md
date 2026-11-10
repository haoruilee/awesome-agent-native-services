---
title: "Nevermined | Agent-Native Services"
service_name: "Nevermined"
description: "The payment layer AI agents actually need"
permalink: /services/nevermined/
page_kind: service
service_slug: "nevermined"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/nevermined.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/nevermined.md"
tagline: "The payment layer AI agents actually need"
website: "https://nevermined.ai/"
repository: "https://github.com/nevermined-io/payments"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://nevermined.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/nevermined-io/payments" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/nevermined.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Skyfire](/services/skyfire/) pairs identity with payments for agents. Nevermined's listing is narrower and sits lower in the stack: an x402 Facilitator that puts payment inside the HTTP exchange itself, so an agent pays for an API call as part of making it.

### Payment inside the request

The dossier walks through the loop. An agent requests a resource. The server answers with HTTP 402 Payment Required and payment terms. The Facilitator pays from the agent's account, the request is retried with cryptographic payment proof attached, and the server delivers the response. There is no checkout page, no redirect, and no human approving each charge.

Around that protocol the dossier lists several billing shapes: prepaid credits that fund an agent's account in advance, usage-based billing per call, token, or request, outcome-based billing that charges on task completion, and dynamic pricing that varies with demand or resource cost. Payment methods named are fiat, crypto, stablecoins including USDC, and prepaid credits. Per-agent accounts carry operator-defined budgets, and transaction history is attributable to each agent.

### SDK and protocol, no MCP

The quickest documented path is the Python SDK, `pip install payments-py`, with source in the [payments repository](https://github.com/nevermined-io/payments) and setup notes in the [SDK getting-started docs](https://docs.nevermined.app/docs/libraries/getting-started/). A REST API covers account management, budget configuration, and transaction history. The catalog has no separate docs URL for Nevermined, so the [Nevermined website](https://nevermined.ai/) is the other starting point.

No standalone MCP server is published, and no Agent Skill. The dossier argues that any MCP-based agent making HTTP calls can benefit from x402 handling transparently. Read that carefully: the 402 response only gets paid if something in the agent's HTTP path understands it.

### What transparent has to mean

In [Commerce & Payments](/categories/commerce-and-payments/), several neighbors work on the same protocol. [OpenLibx402](/services/openlibx402/) is an open-source library for x402 integrations, a lighter dependency if you want the protocol without an account platform. [402xAgent](/services/402xagent/) is the check an agent calls before paying an x402 endpoint, which addresses a risk Nevermined's dossier does not discuss: paying a server you should not trust. [Circle Agent Stack](/services/circle-agent-stack/) describes broader financial infrastructure. The [payments guide](/guides/payments-for-autonomous-agents/) compares these approaches.

Before wiring money into an agent loop, confirm in the vendor's materials which side of the exchange each component runs on, buyer or seller, and what the agent's HTTP client must include to answer a 402. Find out how budgets are enforced when a limit is hit mid-task, how fiat and stablecoin settlement differ, and who decides that an outcome succeeded under outcome-based billing. The dossier does not say. Fees and settlement timing belong to the vendor's current pages.

### Editor's take

Nevermined serves two groups: API and tool sellers who want to charge agents per call inside HTTP, and Python agent builders who want operator budgets around those payments. Teams that only need the protocol should start with OpenLibx402; teams worried about where their agent sends money should add 402xAgent regardless. This is an editor's reading of the dossier, the payments repository, and the SDK docs, and no payment has moved through Nevermined on this project's behalf.

</section>

## What it does

Nevermined's **x402 Facilitator** embeds payment directly into the HTTP protocol. When an agent makes an API request, the server responds with HTTP 402 Payment Required; the agent pays via the x402 protocol and the request is fulfilled — all within a single HTTP exchange. No human checkout flow. No redirect. Payment is part of the API call itself.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, http, API
- **MCP:** ⚠️ Not yet published as standalone MCP server
- **Agent Skill:** ⚠️ No official skill published by Nevermined yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP x402 | Standard 402 response with payment terms; agent-side Facilitator handles payment |
| REST API | Account management, budget configuration, transaction history |
| Payment Methods | Fiat, crypto, stablecoins (USDC), prepaid credits |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
