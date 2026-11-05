---
title: "Vapi | Agent-Native Services"
service_name: "Vapi"
description: "Build advanced voice AI agents"
permalink: /services/vapi/
page_kind: service
service_slug: "vapi"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/vapi.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/vapi.md"
tagline: "Build advanced voice AI agents"
website: "https://vapi.ai"
repository: "https://github.com/VapiAI/server-sdk-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vapi.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.vapi.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/VapiAI/server-sdk-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/vapi.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Vapi is an API platform for building, deploying, and scaling voice AI agents. Developers create voice assistants programmatically, deploy them to phone numbers or web calls, and configure tool-calling so agents can invoke external APIs mid-conversation. The entire voice agent lifecycle — provisioning, routing, call handling, transcription, and analytics — is controlled via API with no human telephone operator in the loop.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, webhook, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official skill published by Vapi yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Full assistant, phone number, call, and analytics management |
| Python SDK | `pip install vapi-server-sdk` |
| TypeScript SDK | `npm install @vapi-ai/server-sdk` |
| Web SDK | Browser-based voice calls |
| Webhooks | `speech-update`, `tool-calls`, `end-of-call-report`, `assistant-request`, `transfer-destination-request` |
| MCP Server | Manage assistants, numbers, and calls via Model Context Protocol |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
