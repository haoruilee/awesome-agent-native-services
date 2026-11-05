---
title: "Novu | Agent-Native Services"
service_name: "Novu"
description: "The open-source notification infrastructure — with an Agent Toolkit for AI agents"
permalink: /services/novu/
page_kind: service
service_slug: "novu"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/novu.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/novu.md"
tagline: "The open-source notification infrastructure — with an Agent Toolkit for AI agents"
website: "https://novu.co"
repository: "https://github.com/novuhq/novu"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-source (MIT) + Novu Cloud</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://novu.co" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.novu.co" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/novuhq/novu" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/novu.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Novu is an open-source notification infrastructure platform with a dedicated **Agent Toolkit** that exposes notification workflows as tools agents can call. An agent needing to send a notification — via email, SMS, Slack, push, in-app, or any other channel — calls a Novu workflow tool; Novu handles channel selection, template rendering, delivery, and preference enforcement.

The agent does not know or care which channel is used. Novu's workflow engine decides based on subscriber preferences and channel availability.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at novuhq/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Node.js SDK | `npm install @novu/node` |
| Python SDK | `pip install novu` |
| REST API | Full workflow management and trigger API |
| MCP Server | Model Context Protocol for direct LLM notification triggering |
| Agent Skills | `npx skills add novuhq/skills` (5 skills covering all notification patterns) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
