---
title: "CosVoice | Agent-Native Services"
service_name: "CosVoice"
description: "Your AI Agent gets its own phone number"
permalink: /services/cosvoice/
page_kind: service
service_slug: "cosvoice"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/cosvoice.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/cosvoice.md"
tagline: "Your AI Agent gets its own phone number"
verified_at: "2026-10-09"
website: "https://cosvoice.com"
repository: "https://github.com/CosVoice/cosvoice-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (packaging repository)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · webhook · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-09</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cosvoice.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://cosvoice.com/skill" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/CosVoice/cosvoice-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/cosvoice.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CosVoice provisions a phone number and an email address for an assistant. The homepage describes three uses: the owner calls or texts the line, the assistant places calls (including booking a table), and the line answers when the owner cannot. After a call, the owner gets a written summary. The skill says the voice is full duplex and that the line says it is an AI assistant when asked.

The agent drives the line over MCP: search numbers, create the line, place a call, poll for the outcome, read transcripts and email, and send email from the line's own address (`handle@bot.cosvoice.com` on the skill page). Calls are asynchronous. The skill says to poll `get_call` or wait for a `call.completed` webhook. A call is capped at 10 minutes. The line never pays and never reads out a card.

Current prices are the live pricing page and the skill page, checked 2026-10-09: Starter $29/month with 100 minutes, Plus $79/month with 300 minutes, Pro $199/month with 1,000 minutes, overage $0.25 per minute on paid plans. A 7-day trial is described as $0, with a card on file, then $29 for Starter unless the owner cancels or moves plans. The packaging README still lists older bundles (Starter 60 minutes, Plus $69/200, Pro $149/600). Those README figures are not the live page.

The skill says calls and texts go to US and Canada numbers only. The pricing page says available numbers are US area codes and that Canada is next. One new number per paid month per plan is the skill's account rule.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, webhook, openapi, http, API
- **MCP:** ✅ Available — auth required
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://cosvoice.com/skill and follow the instructions to connect CosVoice.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/cosvoice.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL onboarding | https://cosvoice.com/skill |
| MCP | `https://cosvoice.com/mcp` (Streamable HTTP, OAuth or bearer) |
| OpenAPI | https://cosvoice.com/openapi.json — REST base `https://cosvoice.com/api/v1` |
| OAuth discovery | `/.well-known/oauth-protected-resource` and `/.well-known/oauth-authorization-server` |
| Webhook | `set_webhook` for `call.completed`, and `set_bot_push` for assistant wakeups, as written on the skill page |
| Registry | `com.cosvoice/cosvoice` |

---

## Verification

Last verified **2026-10-09**.

Sources:
- https://cosvoice.com
- https://cosvoice.com/skill
- https://cosvoice.com/mcp
- https://github.com/CosVoice/cosvoice-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
