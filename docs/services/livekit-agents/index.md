---
title: "LiveKit Agents | Agent-Native Services"
service_name: "LiveKit Agents"
description: "Build, run, and observe AI agents — voice, video, and physical AI on LiveKit"
permalink: /services/livekit-agents/
page_kind: service
service_slug: "livekit-agents"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/livekit-agents.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/livekit-agents.md"
tagline: "Build, run, and observe AI agents — voice, video, and physical AI on LiveKit"
website: "https://livekit.com/agents"
repository: "https://github.com/livekit/agents"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://livekit.com/agents" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.livekit.io/agents/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/livekit/agents" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/livekit-agents.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

LiveKit **Agents** is a framework and cloud platform for **real-time voice (and video) AI agents**: **STT → LLM → TTS** pipelines with **VAD**, **turn detection**, **barge-in**, **noise cancellation**, and **tool use** during live sessions. **LiveKit Cloud** provides global **WebRTC** media mesh, **autoscaling**, **SIP telephony**, **session replay**, **metrics**, and **logs** — infrastructure aimed at **conversational agents**, not traditional CRUD APIs.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK
- **MCP:** ⚠️ Not primarily an MCP product; integration is SDK + WebRTC + SIP.
- **Agent Skill:** ⚠️ LiveKit publishes coding agent resources (Claude Code, Cursor, etc.) per marketing site; no single npx skills add livekit/... verified in-repo — see LiveKit docs Coding agent resources.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
# Follow https://docs.livekit.io/agents/start/voice-ai/
# Typical: pip install livekit-agents + plugins (STT, LLM, TTS), then livekit agents CLI
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/livekit-agents.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python | `livekit-agents` + plugins — see GitHub |
| TypeScript | Agents SDK — see docs |
| WebRTC | Client SDKs (web, iOS, Android) |
| SIP | Telephony product — see LiveKit Phone Numbers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
