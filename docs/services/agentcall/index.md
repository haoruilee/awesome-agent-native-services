---
title: "AgentCall | Agent-Native Services"
service_name: "AgentCall"
description: "Your AI agent, in every meeting"
permalink: /services/agentcall/
page_kind: service
service_slug: "agentcall"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/agentcall.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/agentcall.md"
tagline: "Your AI agent, in every meeting"
verified_at: "2026-09-30"
website: "https://agentcall.dev"
repository: "https://github.com/pattern-ai-labs/agentcall"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (skill package)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · REST · websocket · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentcall.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/pattern-ai-labs/agentcall#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/pattern-ai-labs/agentcall" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/agentcall.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentCall turns a coding agent into a meeting participant. The bot talks (TTS), listens (live transcripts), can screenshot or screenshare, shows an optional avatar, and keeps the agent's full local context — it can still search code and run commands while in the call. Platforms: Google Meet, Zoom, Microsoft Teams. Distributed as an Agent Skill, not a human-imported client library.

---

## Agent-facing interfaces

- **Interaction pattern:** Agent Skill (not an SDK)
- **Catalog protocols:** Agent Skill, REST, websocket, http, API
- **MCP:** ⚠️ Not published
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Agent Skill (not an SDK)

```text
/plugin marketplace add pattern-ai-labs/agentcall
/plugin install join-meeting@agentcall
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/agentcall.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Skill / plugin | `join-meeting@agentcall`, OpenClaw, Gemini extension, raw `SKILL.md` |
| REST + WebSocket | `api.agentcall.dev` |
| Dashboard | https://app.agentcall.dev |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://agentcall.dev

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
