---
title: "PlaceCall | Agent-Native Services"
service_name: "PlaceCall"
description: "Give your agent a phone"
permalink: /services/placecall/
page_kind: service
service_slug: "placecall"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/placecall.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/placecall.md"
tagline: "Give your agent a phone"
verified_at: "2026-11-07"
website: "https://voygr.tech/placecall/"
repository: "https://github.com/voygr-tech/placecall"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (client packaging repository; hosted service is closed source)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-07</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://voygr.tech/placecall/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://api.voygr.tech/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/voygr-tech/placecall" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/placecall.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

PlaceCall is a hosted outbound phone layer for agents. The calling agent supplies a US phone number (or a place description) and a plain-language `brief`. PlaceCall dials, navigates IVRs and hold, conducts the conversation, and returns a labelled outcome, transcript, and recording. When the call agent needs a detail the brief lacks, it raises a mid-call question that the calling agent answers while the call is still live.

There is no human calling app: the product is the tool an agent invokes. Self-serve signup creates an account with free credits (250 free calls on a new API key per the site); after that, billing is per successful outcome, not per minute. Destination policy is US numbers only, with some states refused server-side before dialing.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP + published Agent Skills
- **Catalog protocols:** Agent Skill, MCP, REST, openapi, http, API
- **MCP:** ✅ Available — auth required
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** MCP + published Agent Skills

```
https://api.voygr.tech/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/placecall.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://api.voygr.tech/mcp` (Streamable HTTP, OAuth or API key) |
| REST / OpenAPI | https://api.voygr.tech/openapi.json — docs at https://api.voygr.tech/docs |
| Agent Skill | `skills/placecall/SKILL.md` in voygr-tech/placecall; ClawHub / `npx skills add` routes |
| Plugins | Claude Code marketplace, Codex / Cursor plugins, Claude connector, ChatGPT plugin directory |
| Registry | `io.github.voygr-tech/placecall` |

---

## Verification

Last verified **2026-11-07**.

Sources:
- https://voygr.tech/placecall/
- https://api.voygr.tech/mcp
- https://api.voygr.tech/openapi.json
- https://github.com/voygr-tech/placecall

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
