---
title: "AgentMail | Agent-Native Services"
service_name: "AgentMail"
description: "Email for AI agents"
permalink: /services/agentmail/
page_kind: service
service_slug: "agentmail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agentmail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentmail.md"
tagline: "Email for AI agents"
website: "https://agentmail.to"
repository: "https://github.com/agentmail-to"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentmail.to" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.agentmail.to" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentmail-to" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentmail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentMail is an email inbox API built for AI agents to **own** email identities. Rather than proxying through a human's Gmail or Outlook account, agents create dedicated inboxes via API, receive emails via webhook, participate in threaded conversations, and send replies — all without any human mail client in the loop.

The core abstraction is: **the agent is the first-class internet entity at the email address**. AgentMail makes that concrete.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, webhook, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official skill published by AgentMail yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Full CRUD on inboxes, messages, threads |
| Python SDK | `pip install agentmail` |
| TypeScript SDK | `npm install agentmail` |
| MCP Server | Model Context Protocol integration for direct LLM tool use |
| Webhooks | Push notification on inbound email events |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
