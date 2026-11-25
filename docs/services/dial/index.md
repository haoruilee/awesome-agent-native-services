---
title: "Dial | Agent-Native Services"
service_name: "Dial"
description: "Your agent needs a number"
permalink: /services/dial/
page_kind: service
service_slug: "dial"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/dial.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/dial.md"
tagline: "Your agent needs a number"
verified_at: "2026-11-25"
website: "https://getdial.ai"
repository: "https://github.com/GetDial-AI/cli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT declared in package.json and the README only; there is no LICENSE file in the GetDial-AI/cli tree (GitHub detects no license). The hosted service is closed source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · webhook · CLI · SDK · openapi · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://getdial.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.getdial.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/GetDial-AI/cli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/dial.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Dial gives an agent real phone numbers it controls: send and receive SMS, iMessage and WhatsApp, place and answer AI voice calls, and get inbound messages and completed calls back as events. One number can carry several channels, and `lookup_number` tells the agent which channels a recipient can receive on.

Calls run on a Dial-hosted voice agent from a plain-language instruction, or in Self-Hosted mode on the builder's own LLM or audio stack over WebSocket. After a call the agent reads the status and transcript with `get_call`. Inbound calls are answered by the number's inbound instruction, and can be limited to known callers with allow lists.

Pricing on https://getdial.ai/pricing (checked 2026-11-25): pay-as-you-go at $3 per number per month plus metered calls and messages, with a $5 starting credit and no card required; spend pauses at $0. iMessage and WhatsApp need a Local number with add-ons, or the All channels plan. Accounts that have not topped up are capped at 5 minutes per call and 2 concurrent calls.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, webhook, CLI, SDK, openapi, STDIO, http, API
- **MCP:** ✅ Available — auth required
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Read https://getdial.ai/skills.md and follow the instructions to get a Dial phone number.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/dial.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL onboarding | https://getdial.ai/skills.md |
| MCP | `https://getdial.ai/mcp` (Streamable HTTP, OAuth) · `npx @getdial/cli mcp` (stdio) |
| REST | `https://api.getdial.ai`, Bearer key; OpenAPI 3.1 at https://docs.getdial.ai/openapi.json |
| CLI | `dial` (npm `@getdial/cli`), `--json` output |
| SDKs | Node `@getdial/sdk`, Python; LangChain, Vercel AI SDK, CrewAI, AutoGen and Microsoft Agent Framework integrations |
| Events | Signed webhooks (HMAC) and a live account event stream |
| Docs for agents | https://docs.getdial.ai/llms.txt (append `.md` to any docs URL) |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://getdial.ai
- https://getdial.ai/skills.md
- https://getdial.ai/pricing
- https://docs.getdial.ai
- https://docs.getdial.ai/openapi.json
- https://getdial.ai/mcp
- https://getdial.ai/.well-known/oauth-protected-resource/mcp
- https://github.com/GetDial-AI/cli

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
