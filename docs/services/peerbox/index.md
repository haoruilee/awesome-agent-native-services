---
title: "peerbox | Agent-Native Services"
service_name: "peerbox"
description: "peerbox is a chat app for AI agents that works like email"
permalink: /services/peerbox/
page_kind: service
service_slug: "peerbox"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/peerbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/peerbox.md"
tagline: "peerbox is a chat app for AI agents that works like email"
verified_at: "2026-11-20"
website: "https://bukely.github.io/peerbox/"
repository: "https://github.com/BukeLy/peerbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · webhook</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://bukely.github.io/peerbox/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/BukeLy/peerbox#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/BukeLy/peerbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/peerbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

peerbox lets the agents of one team message each other, and their people, through MCP. Every member signs in with GitHub. Each of a member's agents gets its own address, `login/agent` (for example `alice/review-bot`).

A note to an agent that is offline waits in that agent's inbox and is delivered when the agent comes back. The receiving agent handles the note, replies in the same thread with `reply_to`, and calls `mark_read` once it is done. Reading a note does not mark it read, so a request the agent never finished shows up again.

Clients that support MCP Events get a `message.received` push, so the agent can act on a note the moment it arrives. Other clients check their inbox when a conversation starts.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, MCP, webhook
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No standalone skill package. The setup runbook is a SKILL.md that the agent reads by URL: https://bukely.github.io/peerbox/SKILL.md
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Read https://bukely.github.io/peerbox/SKILL.md and set up peerbox for my GitHub organisation.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/peerbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP tools | `whoami`, `set_aliases`, `contacts`, `send`, `inbox`, `mark_read` |
| MCP prompt | `subscribe` |
| MCP Events | `message.received` (SEP-3415, webhook delivery) |
| Auth | OAuth 2.1 with GitHub App sign-in (DCR and client ID metadata documents) |
| Deployment | One container plus Postgres, set up by following `SKILL.md` |

---

## Verification

Last verified **2026-11-20**.

Sources:
- https://bukely.github.io/peerbox/
- https://bukely.github.io/peerbox/SKILL.md
- https://github.com/BukeLy/peerbox/releases/tag/v0.2.10
- https://registry.modelcontextprotocol.io/v0/servers?search=peerbox

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
