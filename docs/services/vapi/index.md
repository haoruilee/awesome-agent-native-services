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

<section class="service-essay" aria-label="Editorial" markdown="1">

Pipecat asks you to assemble the voice pipeline. Vapi asks you to define an assistant and attach a phone number. The tagline is "Build advanced voice AI agents." The dossier's objects are a voice assistant with a model, a voice, and tools; a phone number scoped to that assistant; tool calls during the live call; server webhooks for speech, tools, and call end; and a web call that is not a phone call at all. There is a REST API, Python and TypeScript SDKs, a web SDK, and an MCP server. The Python repo on the entry is [VapiAI/server-sdk-python](https://github.com/VapiAI/server-sdk-python). Docs are [docs.vapi.ai](https://docs.vapi.ai). No Agent Skill is recorded. The lifecycle the entry claims — provision, route, handle, transcribe, measure — is API-controlled, with no telephone operator in the loop.

Per-assistant IDs and per-call traces are the audit. A number belongs to an assistant. That is a narrower delegation than a trunk that can dial anything, and you should confirm the scoping in the docs before you believe the narrower reading. Voice simulation is listed as automated testing with simulated callers, meant to catch bad behavior before deployment. The dossier does not show how a simulation is invoked or what it compares. Mid-call tools are described as OpenAI-style function calls. The webhook is how your server hears them. If the webhook is down, the call still exists. The entry does not say whether the tool failure is spoken to the caller or dropped.

[Voice & Phone](/categories/voice-and-phone/) splits framework from platform. [Pipecat](/services/pipecat/) is the open-source Python pipeline, STT to model to TTS, with WebRTC or SIP and no MCP server. [LiveKit Agents](/services/livekit-agents/) is the other framework, on LiveKit's media. [CosVoice](/services/cosvoice/), [Patter](/services/patter/), and [PlaceCall](/services/placecall/) lead with giving the agent a number, which Vapi also does, inside a larger assistant API. If you want to own the audio pipeline and pick every vendor, Pipecat is the listing. If you want an assistant resource, a number, and webhooks, Vapi is the one whose dossier is that shape. The category has no voice guide. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) is the criterion page.

### Numbers, webhooks, and the scale sentence

The dossier includes a scale claim about call volume. It is omitted here. Capacity, regions, and price belong on the current Vapi docs. Confirm how a number is purchased, whether outbound dialing is a separate permission, and what the MCP server can do relative to the REST API. An MCP tool that can place calls is a delegation sitting in a coding agent's config. Per-call logs may contain audio or transcripts. Read the retention note before you record customers. Simulation is not a substitute for that reading.

### Editor's take

Vapi fits a product that needs voice assistants defined and deployed through an API, including phone numbers and mid-call tools, and that would rather not assemble STT and TTS by hand. It is a heavy dependency for a local prototype Pipecat can host in one Python process. This catalog has not placed a call. The judgement is the object model in the dossier plus the docs URL, with the vendor's volume language left out.

</section>

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
