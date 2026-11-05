---
title: "Patter | Agent-Native Services"
service_name: "Patter"
description: "Patter is the open-source SDK that gives your AI agent a phone number"
permalink: /services/patter/
page_kind: service
service_slug: "patter"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/patter.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/patter.md"
tagline: "Patter is the open-source SDK that gives your AI agent a phone number"
verified_at: "2026-09-30"
website: "https://getpatter.com"
repository: "https://github.com/PatterAI/Patter"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://getpatter.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.getpatter.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/PatterAI/Patter" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/patter.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Patter is an open-source voice stack between an application and the phone network. It runs the agent loop and lets you swap LLM, STT, TTS, realtime, and carrier providers (Twilio, Telnyx, Plivo). Modes: Realtime, Pipeline, Hybrid. Built-in tools, transfer, guardrails, and OpenTelemetry traces are vendor-neutral across carriers. Same API in Python and TypeScript.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + published Agent Skills
- **Catalog protocols:** Agent Skill, http
- **MCP:** ⚠️ Not published
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** SDK + published Agent Skills

```bash
npx skills add patterai/skills
npm install getpatter
# or
pip install getpatter
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/patter.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| npm | `getpatter` |
| PyPI | `getpatter` |
| Skills | `npx skills add patterai/skills` |
| Docs | https://docs.getpatter.com |
| Templates | Separate example repos listed in the README |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/PatterAI/skills
- https://getpatter.com
- https://docs.getpatter.com

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
