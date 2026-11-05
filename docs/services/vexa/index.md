---
title: "Vexa | Agent-Native Services"
service_name: "Vexa"
description: "Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents…"
permalink: /services/vexa/
page_kind: service
service_slug: "vexa"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/vexa.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/vexa.md"
tagline: "Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS"
website: "https://vexa.ai"
repository: "https://github.com/Vexa-ai/vexa"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · websocket · CLI · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vexa.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Vexa-ai/vexa#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Vexa-ai/vexa" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/vexa.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Vexa is an **open-source meeting bot platform** that lets an agent send a bot into Google Meet, Microsoft Teams, or Zoom, capture real-time diarized transcripts (REST + WebSocket), and — distinctively — let the bot **speak and share its screen** mid-meeting. The MCP server exposes 17 tools so any MCP-compatible agent (Claude Desktop, Cursor, etc.) can drive the bot end-to-end.

It is positioned by its maintainers as an explicit open-source alternative to Recall.ai / Otter.ai / Fireflies.ai. The differentiators against the existing entries in this catalog (Recall.ai, Meeting BaaS, MeetStream — all SaaS) are:

- **Self-host** — data never leaves your infrastructure.
- **Interactive bot** — the bot can speak (TTS) and share content, not just listen.
- **First-party MCP** — 17 tools usable from any MCP host without writing REST glue.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, websocket, CLI, API
- **MCP:** ✅ Available — first-party MCP server with 17 tools.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `cli`

## How agents onboard

```
# Self-hosted:
git clone https://github.com/Vexa-ai/vexa
cd vexa && docker compose up -d

# Or hosted SaaS via vexa.ai

# Send a bot to a meeting:
curl -X POST https://<host>/v1/bots \
  -H "X-API-Key: $KEY" \
  -d '{"meeting_url":"https://meet.google.com/abc-defg-hij","platform":"google_meet"}'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/vexa.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Bot CRUD, transcript download |
| WebSocket | Real-time diarized transcript stream |
| MCP server | 17 tools for full bot control |
| Self-host | Docker Compose / Helm |
| Hosted SaaS | vexa.ai |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
