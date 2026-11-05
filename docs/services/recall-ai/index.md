---
title: "Recall.ai | Agent-Native Services"
service_name: "Recall.ai"
description: "The meeting bot API for every platform"
permalink: /services/recall-ai/
page_kind: service
service_slug: "recall-ai"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/recall-ai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/recall-ai.md"
tagline: "The meeting bot API for every platform"
website: "https://recall.ai"
repository: "https://github.com/recallai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · webhook · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://recall.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.recall.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/recallai" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/recall-ai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Recall.ai provides a unified API for deploying bots into Zoom, Google Meet, Microsoft Teams, Webex, Slack Huddles, and GoTo Meeting. Agents create bots via API, bots join scheduled or live meetings, and Recall.ai streams back real-time speaker-diarized transcripts, audio/video, and meeting metadata within 10 seconds — all without a human operating a meeting client.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, webhook, API, documentation
- **MCP:** ⚠️ No dedicated MCP server from Recall.ai
- **Agent Skill:** ⚠️ No official skill published by Recall.ai yet.
- **Onboarding type:** `documentation`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Bot lifecycle: create, list, retrieve, delete |
| Webhooks | Real-time events: transcript segments, participant join/leave, recording status |
| Calendar Integration API V1 | Basic calendar connection and auto-scheduling |
| Calendar Integration API V2 | Granular per-event configuration, advanced edge case handling |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
