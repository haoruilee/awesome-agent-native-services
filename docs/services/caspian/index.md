---
title: "Caspian | Agent-Native Services"
service_name: "Caspian"
description: "Agent communication SDK. The open-source agent communication layer for AI agents — email, WhatsApp, Slack, Discord, Telegram, SMS"
permalink: /services/caspian/
page_kind: service
service_slug: "caspian"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/caspian.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/caspian.md"
tagline: "Agent communication SDK. The open-source agent communication layer for AI agents — email, WhatsApp, Slack, Discord, Telegram, SMS"
verified_at: "2026-09-26"
website: "https://trycaspianai.com"
repository: "https://github.com/TryCaspian/caspian-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">The root repository is AGPL-3.0 according to its actual LICENSE and GitHub metadata, despite the root README&#x27;s Apache-2.0 badge/text. The Python and TypeScript SDK subdirectories separately carry MIT license files; verify the scope of the artifact you use.</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Planned</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · webhook · CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://trycaspianai.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://api.trycaspianai.com/SKILL.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/TryCaspian/caspian-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/caspian.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Caspian gives one AI agent a normalized communication layer across email, Slack, Discord, Telegram, GitHub, Instagram, Facebook Messenger, X, Bluesky, and additional hosted channels. The agent uses one message handler and one reply abstraction while adapters handle platform payloads, thread routing, signature verification, reconnection, and capability differences.

Its defining model is that channels are transports rather than separate identities. Caspian can scope connections to explicit customer and agent records, deliver ordered events with conversation and connection identifiers, and return channel-specific etiquette through `behavior_prompt()` for the model's context.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, webhook, CLI, SDK, http, API
- **MCP:** ⚠️ Not yet published. The official roadmap lists an MCP server as future work; the current verified surfaces are URL onboarding, SDKs, CLI, REST/event APIs, and webhooks.
- **Agent Skill:** ✅ Available — both a live URL-onboarding skill and an official ClawHub package are documented upstream.
- **Onboarding type:** `url`

## How agents onboard

```text
Integrate Caspian so my agent can message people on email, Slack, Discord, Telegram, and more.
Read https://api.trycaspianai.com/SKILL.md and follow it end to end.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/caspian.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **URL onboarding** | Live machine-readable guide at https://api.trycaspianai.com/SKILL.md |
| **Python SDK** | `caspian-sdk` on PyPI; `CommClient`, channel connects, messages, events, and webhooks |
| **TypeScript SDK** | `caspian-sdk` on npm with the same contract and camelCase API |
| **CLI** | `caspian-cli` for project initialization, channel connection, and event tailing |
| **REST / events** | Hosted or self-hosted gateway, including ordered `/v1/events` access |
| **Webhooks** | Signed inbound webhook ingestion and serverless `handle_webhook()` dispatch |
| **MCP** | Not yet shipped; listed on the official roadmap |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/TryCaspian/caspian-sdk/releases/tag/v0.1.2
- https://api.trycaspianai.com/SKILL.md
- https://api.github.com/repos/TryCaspian/caspian-sdk

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
