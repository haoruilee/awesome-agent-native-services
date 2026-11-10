---
title: "Pipecat | Agent-Native Services"
service_name: "Pipecat"
description: "Open-source framework for real-time voice AI agents"
permalink: /services/pipecat/
page_kind: service
service_slug: "pipecat"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/pipecat.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/pipecat.md"
tagline: "Open-source framework for real-time voice AI agents"
website: "https://pipecat.ai"
repository: "https://github.com/pipecat-ai/pipecat"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://pipecat.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.pipecat.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/pipecat-ai/pipecat" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/pipecat.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Start with the transport. A voice agent built this way runs as a Python process attached to a WebRTC or SIP connection, and someone has to host that process. The dossier names a Python SDK, those two transports, and plugin adapters. There is no standalone MCP server and no Agent Skill. Pipecat is a framework your code imports, not a service your agent calls.

### A pipeline, not a phone number

The tagline is "Open-source framework for real-time voice AI agents." The dossier's How to Use section describes the shape: build a pipeline of speech-to-text, LLM, and text-to-speech, attach a transport, then run headless agent workers for live calls. The listed primitives are the realtime voice pipeline, turn detection, and in-call tool invocation.

Turn detection is often the hard part. Deciding when a caller has finished speaking, and what to do when they interrupt, determines whether the agent is usable on a real call. Having it as a named primitive is the main reason to start from a framework rather than wiring speech providers together yourself.

Identity is described as per-agent runtime identity plus provider credentials. In practice your speech, model, and telephony keys define what the agent can do. Escalation to a human can be added when confidence or intent thresholds are crossed, but the dossier presents it as something you build.

### Framework or hosted voice

[Voice & Phone](/categories/voice-and-phone/) splits roughly in two. [Vapi](/services/vapi/) is listed as a platform for building voice agents, and [CosVoice](/services/cosvoice/) and [PlaceCall](/services/placecall/) give an existing agent a phone. Those reduce the code you own. [LiveKit Agents](/services/livekit-agents/) and [Patter](/services/patter/) sit nearer to Pipecat as SDKs that run in your process. LiveKit pairs its agent framework with its own media infrastructure, while the dossier describes Pipecat as transport-pluggable.

That flexibility cuts both ways. You choose the speech-to-text, model, and voice providers, and you also own their failure modes. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why a framework qualifies for the catalog: what it produces is an agent loop that reasons and acts during the call.

### Checks before a live call

Look up which providers the plugin adapters currently cover in the [Pipecat docs](https://docs.pipecat.ai). Decide who operates the workers and the SIP trunk, because the dossier leaves hosting to you. Confirm how tool calls behave mid-utterance and how a call is handed to a person. Responsiveness depends on your provider choices and deployment, so measure it in your own setup rather than relying on a published figure.

### Editor's take

Pipecat fits a team with Python engineers who want to own the voice stack and swap providers freely. If you want an agent answering a phone number with little code of your own, CosVoice, PlaceCall, or Vapi is the shorter path. If you already run LiveKit for media, its agent framework is the natural comparison. This is an opinion drawn from the dossier and the public docs; the project has not built or run a Pipecat pipeline.

</section>

## What it does

Provides low-latency orchestration for realtime speech processing, tool calling, and conversational turn management.

## Agent-facing interfaces

- **Catalog protocols:** SDK
- **MCP:** ⚠️ No standalone official MCP server package.
- **Agent Skill:** ⚠️ No official AgentSkills package found.
- **Onboarding type:** `other`

## Protocol surface

Python SDK, WebRTC/SIP transports, plugin adapters.

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
