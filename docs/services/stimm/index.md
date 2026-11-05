---
title: "Stimm | Agent-Native Services"
service_name: "Stimm"
description: "The Open Source Voice Agent Platform. Orchestrate ultra-low latency AI pipelines for real-time conversations over WebRTC"
permalink: /services/stimm/
page_kind: service
service_slug: "stimm"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/stimm.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/stimm.md"
tagline: "The Open Source Voice Agent Platform. Orchestrate ultra-low latency AI pipelines for real-time conversations over WebRTC"
website: "https://stimm.ai"
repository: "https://github.com/stimm-ai/stimm"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open source · early-stage but rapid 2026 iteration</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://stimm.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/stimm-ai/stimm#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/stimm-ai/stimm" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/stimm.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Stimm is an **open-source orchestrator for real-time voice agents** over WebRTC. Its design center is **ultra-low latency** with two distinguishing primitives:

1. **Dual-agent architecture** — a small, fast agent handles immediate verbal feedback (filler / acknowledgment) while a larger, slower agent handles the substantive reasoning. The pipeline coordinates the two so the user never feels a long silence.
2. **Optimistic VUI** — speak interim feedback before the full LLM response is finalized, cancel or amend if reasoning diverges.

Operators bring their own STT, LLM, and TTS providers; Stimm orchestrates the WebRTC media plane and the dual-agent control plane. It is an open-source contender to LiveKit Agents and the closed-source Vapi / Retell, with a tighter focus on perceived-latency engineering.

---

## Agent-facing interfaces

- **Catalog protocols:** API, documentation
- **MCP:** ⚠️ Not yet published as a first-party MCP server.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `documentation`

## How agents onboard

```
git clone https://github.com/stimm-ai/stimm
# follow README to install + run the orchestrator
# then connect your STT / LLM / TTS providers and a WebRTC client
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/stimm.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| WebRTC | Real-time audio media plane |
| Orchestrator API | Pipeline configuration, session lifecycle |
| Provider adapters | STT, LLM, TTS — pluggable |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
