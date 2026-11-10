---
title: "Skyfire | Agent-Native Services"
service_name: "Skyfire"
description: "Identity and payments for autonomous AI agents"
permalink: /services/skyfire/
page_kind: service
service_slug: "skyfire"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/skyfire.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md"
tagline: "Identity and payments for autonomous AI agents"
website: "https://skyfire.xyz"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://skyfire.xyz" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent that pays for a service needs an identity the service will accept and a wallet that cannot spend the whole balance because the model felt like it. Skyfire's tagline is "Identity and payments for autonomous AI agents." The dossier's primitives are a Know Your Agent token, an agent wallet, programmable spend limits set by an operator, a KYAPay protocol described as OAuth2 and OIDC compatible, an agent checkout, and a behavioral record of transactions. Agents are supposed to sign up, authenticate, and pay without a person in the transaction. Service providers are the other side: they can charge agents and receive fraud signals. The surface is a REST API. MCP is unavailable. There is no Agent Skill. The website on the entry is [skyfire.xyz](https://skyfire.xyz). The dossier does not list a separate docs URL or a GitHub repository. That absence is part of the evaluation. The public site has to be enough to find the API, or it is not.

Spend limits are the control plane. The entry says they exist as per-agent budgets and per-transaction caps. It does not show the fields. "Zero human intervention" is the happy path inside those caps, not a promise that an unset cap is safe. The behavioral record is an immutable log the dossier says builds a reputation. Who can read it, and whether a new agent inherits anything, is not specified.

[Payments for autonomous agents](/guides/payments-for-autonomous-agents/) keeps identity, wallets, HTTP 402, and mandates apart. Skyfire is the identity-and-wallet network, not a 402 middleware library. [OpenLibx402](/services/openlibx402/) is that library, embedded in your FastAPI or Express app. [402xAgent](/services/402xagent/) is the check before an x402 payment. [Circle Agent Stack](/services/circle-agent-stack/) is Circle's wallets, CLI, and gateway. [AgentsPay](/services/agentspay/) is crypto identity and embedded wallets. [Nevermined](/services/nevermined/) is another payment-layer tagline. Skyfire is the listing whose distinctive word is KYA, a token with no human KYC equivalent, which is also one of the examples in [What makes a service agent-native](/guides/what-makes-a-service-agent-native/). The collection is [Commerce & Payments](/categories/commerce-and-payments/).

### Find the API before you believe the protocol name

KYAPay is called an open standard in the dossier and is not given a specification link in the catalog entry. Search the vendor site for the protocol document, the token format, and how a service provider verifies it. If the only page is a marketing homepage, the integration claim is ahead of the artifact. Confirm how a wallet is funded, who can lower a spend cap, and what an agent can still do after the cap is hit. No chain, token, or fee is stated here, and none should be inferred from the word wallet.

### Editor's take

Skyfire fits an operator who needs a verified agent identity and a budgeted wallet, and who can find a real API on the vendor site to match this dossier. It is the wrong tool if you only need to answer HTTP 402 from a server you run, and it is an incomplete listing if the public docs never appear. This project has not created a KYA token or paid through KYAPay. The opinion is the primitive list, bounded by the missing docs URL.

</section>

## What it does

Skyfire is a payment network and identity infrastructure built from the ground up for autonomous AI agents. It provides **Know Your Agent (KYA)** verified identities, agent wallets with programmable spend controls, and an open **KYAPay protocol** — so agents can sign up for services, authenticate, and pay without any human in the transaction loop. Service providers can monetize AI agent access directly, treating agents as a new class of verified customer.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, API
- **MCP:** ⚠️ Not yet publicly documented
- **Agent Skill:** ⚠️ No official skill published by Skyfire yet.
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Wallet management, payment execution, identity operations |
| OAuth2/OIDC | Standard auth protocol extended for agent identity |
| KYAPay Protocol | Open standard for agent checkout — any service can implement receiver side |
| Agent Checkout | Standardized UI/API flow for agent-to-service transactions |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
