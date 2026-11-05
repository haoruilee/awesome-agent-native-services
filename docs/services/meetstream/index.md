---
title: "MeetStream | Agent-Native Services"
service_name: "MeetStream"
description: "API & Infrastructure to capture recordings, transcripts & metadata from meetings"
permalink: /services/meetstream/
page_kind: service
service_slug: "meetstream"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/meetstream.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meetstream.md"
tagline: "API & Infrastructure to capture recordings, transcripts & metadata from meetings"
website: "https://meetstream.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · websocket · webhook · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://meetstream.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.meetstream.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meetstream.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MeetStream provides a **unified meeting-bot API** to join **Zoom, Google Meet, and Microsoft Teams**, capture **recordings and real-time audio/video**, stream **speaker-attributed transcripts** (live and async), expose **participant and chat metadata**, and support **interactive agents** (e.g., TTS, chat, display) — so downstream **AI agents** consume structured meeting data without building per-platform media pipelines.

---

## Agent-facing interfaces

- **Interaction pattern:** REST + Webhooks + WebSockets (real-time media/transcripts)
- **Catalog protocols:** MCP, REST, websocket, webhook, CLI, http, API
- **MCP:** ✅ Available (documentation MCP)
- **Agent Skill:** ⚠️ No npx skills add … registry entry — MeetStream publishes a downloadable Claude Skill (ZIP with SKILL.md) for API patterns, webhooks, and WebSockets.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** REST + Webhooks + WebSockets (real-time media/transcripts)

```bash
curl -X POST "https://api.meetstream.ai/api/v1/bots/create_bot" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"meeting_link":"https://meet.google.com/xxx-xxxx-xxx","bot_name":"Meetstream Agent","video_required":true}'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meetstream.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Bot lifecycle, transcripts, metadata — [docs.meetstream.ai](https://docs.meetstream.ai) |
| Webhooks | Live events (e.g., diarized speech) |
| WebSockets | Real-time audio/video stream consumption |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
