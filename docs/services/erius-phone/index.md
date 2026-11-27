---
title: "ERIUS PHONE | Agent-Native Services"
service_name: "ERIUS PHONE"
description: "Give your AI agent its own Android phone"
permalink: /services/erius-phone/
page_kind: service
service_slug: "erius-phone"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/erius-phone.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/erius-phone.md"
tagline: "Give your AI agent its own Android phone"
verified_at: "2026-11-27"
website: "https://eriusphone.com"
repository: "https://github.com/Protremix/erius-phone-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT for the public MCP server (Copyright 2026 ERIUS). The hosted Android phone service is closed-source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://eriusphone.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://eriusphone.com/docs.html" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Protremix/erius-phone-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/erius-phone.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ERIUS PHONE runs an isolated, persistent cloud Android phone for an agent and exposes that phone over one HTTP API and MCP. The device is Android 13, with the phone profile described as Android 15 / Galaxy S25. The agent reads the screen (`/screenshot`, `/snapshot`, `/observe`) and acts with `/tap`, `/type`, and `/swipe`, plus launch, install, key presses, and crash logs. Apps, sign-ins, and files stay on that phone between sessions. Docs say devices are provisioned for the account — there is no create-device endpoint — and a key can see only that account's devices.

The homepage banner offers one real Android phone for 24 hours at EUR 0. Stripe checks the card and nothing is charged. After the trial, keeping the phone means choosing a plan. `llms.txt` points at https://eriusphone.com/pricing for current euro plans. Voice calls exist as a separate, billed add-on and are excluded from the trial; they are not what this listing is for. The product is the Android device, not a phone number.

---

## Agent-facing interfaces

- **Interaction pattern:** REST API + stdio MCP + remote HTTP MCP, after an operator creates the account and key. ⚠️ Not a one-URL join.
- **Catalog protocols:** MCP, REST, STDIO, http, API
- **MCP:** ✅ Available — local stdio server and a remote POST endpoint
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** REST API + stdio MCP + remote HTTP MCP, after an operator creates the account and key. ⚠️ Not a one-URL join.

```bash
# Person first: https://eriusphone.com/start/
# email confirmation, then a Stripe card check (EUR 0, 24-hour trial). The key arrives by email.
claude mcp add erius-phone \
  -e ERIUS_PHONE_API_KEY="$ERIUS_PHONE_API_KEY" \
  -e ERIUS_PHONE_DEFAULT_DEVICE="your-device-id" \
  -- uvx erius-phone-mcp
# Remote MCP is POST-only: https://api.eriusphone.com/mcp
# Authorization: Bearer $ERIUS_PHONE_API_KEY
# or header X-API-Key: $ERIUS_PHONE_API_KEY
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/erius-phone.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://api.eriusphone.com` — `X-API-Key` or `Authorization: Bearer`. Device routes include `/screenshot`, `/snapshot`, `/observe`, `/tap`, `/type`, `/swipe`. Docs: https://eriusphone.com/docs.html |
| MCP (stdio) | `uvx erius-phone-mcp` — https://github.com/Protremix/erius-phone-mcp |
| MCP (remote) | `POST https://api.eriusphone.com/mcp` — POST only; Bearer realm `erius-phone` |
| Account | `GET /devices`, `GET /whoami` (named in the docs examples) |
| Machine docs | https://eriusphone.com/llms.txt |
| Dashboard | https://eriusphone.com/start/ then the dashboard. The agent does not need the dashboard to drive the phone |

---

## Verification

Last verified **2026-11-27**.

Sources:
- https://eriusphone.com
- https://eriusphone.com/ai-agents/
- https://eriusphone.com/start/
- https://eriusphone.com/llms.txt
- https://eriusphone.com/docs.html
- https://eriusphone.com/security.html
- https://api.eriusphone.com/
- https://api.eriusphone.com/mcp
- https://github.com/Protremix/erius-phone-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
