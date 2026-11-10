---
title: "AgentsPay | Agent-Native Services"
service_name: "AgentsPay"
description: "Crypto identity and embedded wallets for AI agents"
permalink: /services/agentspay/
page_kind: service
service_slug: "agentspay"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/agentspay.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md"
tagline: "Crypto identity and embedded wallets for AI agents"
website: "https://agentspay.dev"
repository: "https://github.com/AgentPayy/agentpayy-platform"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentspay.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/AgentPayy/agentpayy-platform" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Midway through a research task, an agent hits a data API that wants payment or a key it does not have. In most setups the run stops there and waits for a human with a credit card. AgentsPay aims to remove that stop. The site describes it as "Crypto identity and embedded wallets for AI agents," and the dossier explains the pieces: a decentralized identifier for each agent, a stablecoin wallet with an operator-set ceiling, and a gateway that tells the agent what a service costs.

### Paying without a human card

The flow in the dossier runs like this. An operator creates the agent's identity and funds its USDC wallet with a spending ceiling. When the agent meets a service that requires payment, it queries the MCP-native gateway to discover the terms, pays from the wallet within the ceiling, and gets access. The transaction is recorded on-chain against the agent's identifier.

The dossier names three surfaces. The gateway is described as built around the Model Context Protocol over HTTP, with the x402 payment protocol named alongside. A REST API handles wallet management and identity operations. The Base L2 chain holds identity and transaction records. Onboarding is to provision a wallet at the [AgentsPay site](https://agentspay.dev) and then use the gateway. No Agent Skill has been published, and the dossier suggests watching the platform repository for one.

### Identity and spend on one chain

The identity is a W3C DID on Base, which the dossier presents as portable and not tied to one provider. Delegation is the ceiling: the operator sets the maximum, and the agent acts freely below it. Audit is the chain itself, which is tamper-evident but also public, a property worth thinking about if payment patterns reveal what your agent is working on.

The record leaves several practical questions to the vendor. How is the wallet's key held, and by whom? Is the ceiling per transaction, per period, or lifetime? Can it be changed or frozen quickly if an agent misbehaves? Which services accept payment through the gateway today? How do refunds work on a chain that does not reverse? Read the site and repository for current answers, and check any fees there rather than assuming.

### Editor's take

The [commerce and payments collection](/categories/commerce-and-payments/) and the [payments guide](/guides/payments-for-autonomous-agents/) cover several approaches to the same stall. [Skyfire](/services/skyfire/) also pairs identity with payments, using verified Know Your Agent identities and its own protocol instead of an on-chain DID. [Circle Agent Stack](/services/circle-agent-stack/) offers wallets, paid-service discovery, and programmable payments with guardrails. [OpenLibx402](/services/openlibx402/) is a library for building x402 integrations yourself, and [402xAgent](/services/402xagent/) is a check an agent runs before paying an x402 endpoint, which could sit in front of a wallet like this one. [Nevermined](/services/nevermined/) is another payment layer pitched at agents.

AgentsPay is a reasonable candidate for an operator who wants agent identity, wallet, and spend limit in one package on Base and is comfortable with on-chain records. If you would rather assemble x402 yourself, start with OpenLibx402. If you want agent identity established through a Know Your Agent check instead of a DID, Skyfire is the comparison, and Circle covers similar wallet and discovery ground. The analysis here relies on the dossier, the vendor site, and the repository; nothing was funded, signed, or spent while writing it.

</section>

## What it does

AgentsPay issues **W3C Decentralized Identifiers (DIDs)** to AI agents on the Base L2 blockchain, embeds USDC wallets with operator-set spending limits, and provides an MCP-native API gateway. Agents can discover which services require payment and pay for them directly — solving the common agent failure mode where execution halts when an API key or payment is needed.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, API
- **MCP:** ✅ MCP-Native
- **Agent Skill:** ⚠️ No official skill published by AgentsPay yet.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| MCP-Native API Gateway | Primary interface for service discovery and payment |
| REST API | Wallet management, DID operations |
| Base L2 | On-chain identity and transaction recording |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
