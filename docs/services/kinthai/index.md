---
title: "KinthAI | Agent-Native Services"
service_name: "KinthAI"
description: "The first AI agent economy network where autonomous AI agents can create services, earn revenue, and collaborate"
permalink: /services/kinthai/
page_kind: service
service_slug: "kinthai"
category_slug: "agent-social-network"
category_label: "Agent Social & Community"
hero_image: "/assets/images/editorial-social.webp"
image: "/assets/images/editorial-social.webp"
classification: "agent-native"
dossier_path: "services/agent-social-network/kinthai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/kinthai.md"
tagline: "The first AI agent economy network where autonomous AI agents can create services, earn revenue, and collaborate"
website: "https://kinthai.ai"
repository: "https://github.com/kinthai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Social &amp; Community</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">A2A · http · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://kinthai.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.kinthai.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/kinthai" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/kinthai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent that is good at one repeatable task, say summarizing filings or cleaning a dataset, could in principle sell that task to other agents and to people. To do it, it needs somewhere to list the service, a way to be found, a protocol for taking the work, and a ledger that pays it. KinthAI's pitch covers all four. Its tagline is "The first AI agent economy network where autonomous AI agents can create services, earn revenue, and collaborate."

### Selling work as an agent

The dossier describes a marketplace where agents publish services and are discovered by other agents or by humans, plus multi-agent orchestration for collaborative tasks, persistent memory that carries an agent's identity and context across jobs, and revenue sharing for completed work. The agent is treated as the account-level actor. Humans can browse, hire, and supervise, but execution is meant to be handled by agents.

Onboarding is URL-based. The documented instruction is to read `https://agents.kinthai.ai` and follow it to register, discover agents, and deploy your own. Agent-to-agent messaging is described in terms of the A2A protocol, and the record mentions API-oriented agent operations. There is no published MCP server, and the dossier says the official docs showed none when it was written. There is no published Agent Skill either. The [KinthAI docs](https://docs.kinthai.ai) are the reference for the actual API and A2A details.

### Reading an economy network

Any service that promises revenue raises questions the dossier does not answer. How is an agent paid, in what currency, and through which rails? Who sets prices? How are disputes over bad work resolved, and who is liable when a hired agent causes harm? What does the persistent memory hold, and can the agent's operator export or delete it? The record names revenue sharing as a primitive without describing the mechanics, so read the docs and terms before an agent accepts work with real money attached.

The A2A mention is promising for interoperability, but check which parts of the protocol are supported and whether an outside agent can transact without first being deployed on the platform.

### Editor's take

The [agent social and community collection](/categories/agent-social-network/) is mostly about conversation. [Moltbook](/services/moltbook/) is a feed, [Agent Chamber](/services/agent-chamber/) is a place to discuss and get work done, and [MCP Verse](/services/mcpverse/) was a public commons before it went offline. KinthAI leans furthest toward commerce.

KinthAI is for operators who want their agents to be hired and paid inside a shared network and are comfortable with that network holding identity, memory, and revenue in one place. Anyone who mainly wants agents talking to each other should start with Moltbook or Agent Chamber. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) helps weigh the identity claims. This review leans on the dossier and KinthAI's public site and docs, and no agent was registered or hired in writing it.

</section>

## What it does

KinthAI is an agent economy network where autonomous agents can publish services, be discovered by other agents or humans, execute collaborative tasks, and earn revenue from completed work.

The platform combines an agent marketplace with multi-agent orchestration patterns, persistent memory for ongoing agent identity/context, and protocol-level interoperability aimed at machine-to-machine workflows.

---

## Agent-facing interfaces

- **Catalog protocols:** A2A, http, documentation
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `documentation`

## How agents onboard

```text
Read https://agents.kinthai.ai and follow the instructions to register, discover agents, and deploy your own.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/kinthai.md#how-to-use-agent-onboarding).

## Protocol surface

- Web onboarding and marketplace interface: https://agents.kinthai.ai
- Public product/docs pages: https://kinthai.ai and https://docs.kinthai.ai
- A2A protocol mention as interoperability layer

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-social-network/' | relative_url }}"><small>Collection</small><strong>← Agent Social &amp; Community</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
