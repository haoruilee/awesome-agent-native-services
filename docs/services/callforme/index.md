---
title: "CallForMe | Agent-Native Services"
service_name: "CallForMe"
description: "Let your agent call businesses for you"
permalink: /services/callforme/
page_kind: service
service_slug: "callforme"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/callforme.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/callforme.md"
tagline: "Let your agent call businesses for you"
verified_at: "2026-11-20"
website: "https://callforme.tel/"
repository: "https://github.com/callforme-tel/callforme"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (README, Agent Skill and manifests; the hosted service is closed source)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · openapi · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://callforme.tel/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://callforme.tel/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/callforme-tel/callforme" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/callforme.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CallForMe places real phone calls to businesses in the US and Canada for the user's agent. The agent supplies a goal, details the business may need, pre-approved answers and limits. A voice assistant dials, says up front that it is an assistant calling for the named person on a recorded line, works phone menus, waits on hold, and returns a structured outcome (type, summary, answers, confirmation codes, price), a transcript and a recording link.

When the business asks something the agent did not cover, the question is pushed back to the agent as a `pending_question` while the call is live. The agent answers with `answer_question` (from what it knows, or by asking the user), and the answer goes straight into the conversation. If no answer arrives in about 45 seconds, the assistant tells the business the person will follow up and carries on.

Pricing is prepaid: $1 per answered call (first 2 minutes), then $0.40 per minute, up to 30 minutes. Unanswered and busy calls are free, as are `plan_call`, `find_business` and the demo lines.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, openapi, http
- **MCP:** ✅ Available — auth required
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Read https://callforme.tel/skill.md and follow the instructions to connect and place a call.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/callforme.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://callforme.tel/mcp` (Streamable HTTP, OAuth 2.1 or Bearer key) |
| REST / OpenAPI | `https://callforme.tel/v1`, spec at https://callforme.tel/openapi.json |
| Agent Skill | https://callforme.tel/skill.md and `skills/callforme/SKILL.md` in callforme-tel/callforme |
| Docs for agents | https://callforme.tel/llms.txt |
| Registry | `tel.callforme/callforme` |

---

## Verification

Last verified **2026-11-20**.

Sources:
- https://callforme.tel/
- https://callforme.tel/mcp
- https://callforme.tel/mcp/open
- https://callforme.tel/openapi.json
- https://callforme.tel/skill.md
- https://github.com/callforme-tel/callforme/tree/main/skills/callforme

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
