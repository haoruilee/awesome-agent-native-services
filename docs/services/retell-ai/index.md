---
title: "Retell AI | Agent-Native Services"
service_name: "Retell AI"
description: "#1 AI Voice Agent Platform for Automating Calls"
permalink: /services/retell-ai/
page_kind: service
service_slug: "retell-ai"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/retell-ai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/retell-ai.md"
tagline: "#1 AI Voice Agent Platform for Automating Calls"
website: "https://www.retellai.com"
repository: "https://github.com/RetellAI/retell-python-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.retellai.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.retellai.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/RetellAI/retell-python-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/retell-ai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Retell is a platform to build, test, deploy, and monitor **AI phone agents**: inbound and outbound calls, custom telephony via SIP, real-time function calling during speech, webhooks for call lifecycle and analytics, and simulation testing before production. The product is scoped around autonomous voice agents—not a human-operated contact center UI as the primary control plane.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + webhooks + optional MCP (mid-call tools and assistant management)
- **Catalog protocols:** MCP, REST, webhook, SDK, http, API
- **MCP:** ✅ Available (product-native)
- **Agent Skill:** ⚠️ No official npx skills add … pack from Retell yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + webhooks + optional MCP (mid-call tools and assistant management)

```bash
pip install retell-sdk
# or: npm install retell-sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/retell-ai.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Call creation, agent management, analytics — see [docs.retellai.com](https://docs.retellai.com) |
| Python SDK | `pip install retell-sdk` — [retell-python-sdk](https://github.com/RetellAI/retell-python-sdk) |
| TypeScript SDK | `npm install retell-sdk` — [retell-typescript-sdk](https://github.com/RetellAI/retell-typescript-sdk) |
| Webhooks | Real-time and post-call events for integrations |
| SIP | Custom telephony interconnection |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
