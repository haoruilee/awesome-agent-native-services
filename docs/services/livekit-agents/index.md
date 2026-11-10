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

<section class="service-essay" aria-label="Editorial" markdown="1">

A voice agent built on this framework is split between two operators. The agent's logic runs as a worker process your team writes in Python or TypeScript. The media mesh, phone numbers, autoscaling, and session replay are offered by LiveKit Cloud. That split decides where a live conversation can break and who gets paged when it does, so it is the first thing to understand.

### Rooms, sessions, and a worker

The dossier describes [LiveKit Agents](https://docs.livekit.io/agents/) as a framework and cloud platform for real-time voice and video agents. The unit of work is a room. A person joins from a browser, a mobile app, or a SIP call. A worker picks up the job and starts an AgentSession, which wires speech-to-text, the model, text-to-speech, voice activity detection, and turn detection into one loop. The agent listens, plans, speaks, and can call tools between turns. Barge-in and noise cancellation are listed as pipeline features, and they are the part a request-response API cannot give a talking agent.

Integration runs through SDKs rather than a tool protocol. The dossier lists the Python package `livekit-agents` with plugins, a TypeScript Agents SDK, a CLI, WebRTC client SDKs for web, iOS, and Android, and SIP. It marks MCP as not the product's surface. On Agent Skills, it notes that LiveKit advertises coding agent resources on its site but that no install command was verified, so the documented starting point is the voice AI quickstart in the docs.

### Where it sits among voice listings

The [Voice & Phone](/categories/voice-and-phone/) category mixes frameworks with phone-number services. [Pipecat](/services/pipecat/), an open-source framework for real-time voice agents, is the closest neighbor; the comparison turns on how much you want LiveKit's cloud underneath by default. [Vapi](/services/vapi/) is pitched as a place to build voice agents rather than a framework you deploy. [Patter](/services/patter/) and [CosVoice](/services/cosvoice/) start from the other end and hand an agent a phone number. LiveKit reaches telephony through SIP and its phone numbers product, but its center of gravity is the room. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a real-time session primitive qualifies.

### Before a production call

Auth comes in two layers. Access tokens admit participants, human or agent, to specific rooms; API keys cover server-side deployment and management. Check how tokens are minted, how long they live, and whether the agent's identity is distinguishable from the caller's in logs and recordings.

Then settle who operates which piece. The dossier does not say how much of the stack runs without LiveKit Cloud, which providers sit behind LiveKit Inference, or what session replay retains. Handing a call to a human is left to application logic. Compliance options are described as available on the cloud, so read the trust center instead of assuming coverage.

### Editor's take

The natural fit is a team that wants to own the agent's code but not media servers or SIP trunks. If the goal is a phone number for an agent that already exists, Patter or CosVoice start closer to that. If you want an open framework with no default cloud attached, compare Pipecat first. These notes come from the catalog dossier and LiveKit's published docs; nobody on this project has put a caller through it.

</section>

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
