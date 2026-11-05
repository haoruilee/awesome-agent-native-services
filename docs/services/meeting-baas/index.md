---
title: "Meeting BaaS | Agent-Native Services"
service_name: "Meeting BaaS"
description: "Meeting Bots As A Service — The developer API for programmatic access to meeting data across Zoom, Google Meet, and Microsoft Teams"
permalink: /services/meeting-baas/
page_kind: service
service_slug: "meeting-baas"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/meeting-baas.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meeting-baas.md"
tagline: "Meeting Bots As A Service — The developer API for programmatic access to meeting data across Zoom, Google Meet, and Microsoft Teams"
website: "https://meetingbaas.com"
repository: "https://github.com/Meeting-Baas"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://meetingbaas.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.meetingbaas.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Meeting-Baas" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meeting-baas.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Meeting BaaS provides a hosted API (with a self-hosting option) to deploy bots into Zoom, Google Meet, and Microsoft Teams from code. An agent or backend posts a meeting URL and configuration; the bot joins, can record, optionally transcribe with speaker-attributed output, and streams status over webhooks. Optional WebSocket streaming exposes raw audio and diarized JSON for real-time agent consumption.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + webhooks + optional MCP
- **Catalog protocols:** MCP, REST, webhook, SDK, http, API
- **MCP:** ✅ Available (official org repo)
- **Agent Skill:** ⚠️ No official SKILL.md / npx skills add … pack from Meeting BaaS yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + webhooks + optional MCP

```bash
curl -X POST "https://api.meetingbaas.com/bots" \
  -H "Content-Type: application/json" \
  -H "x-meeting-baas-api-key: YOUR-API-KEY" \
  -d '{"meeting_url": "YOUR-MEETING-URL", "bot_name": "AI Notetaker", "recording_mode": "speaker_view", "speech_to_text": {"provider": "Default"}}'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meeting-baas.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `POST https://api.meetingbaas.com/bots` — create bot; removal and listing per docs |
| Webhooks (v2) | Account-level, SVIX-signed — `bot.status_change`, `bot.completed`, `bot.failed`, calendar events — [Webhooks (v2)](https://docs.meetingbaas.com/docs/api-v2/webhooks) |
| Callbacks | Per-bot `callback_config` for direct HTTP completion/failure notifications |
| TypeScript SDK | `@meeting-baas/sdk` — `createBaasClient` + `createBot` — [homepage](https://meetingbaas.com/en) |
| MCP | https://github.com/Meeting-Baas/meeting-mcp |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
