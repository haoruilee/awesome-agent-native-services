---
title: "Mobilebox | Agent-Native Services"
service_name: "Mobilebox"
description: "Mobile sandboxes for your AI agents"
permalink: /services/mobilebox/
page_kind: service
service_slug: "mobilebox"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/mobilebox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilebox.md"
tagline: "Mobile sandboxes for your AI agents"
verified_at: "2026-11-25"
website: "https://mobilebox.dev"
repository: "https://github.com/mobilebox-dev/mobilebox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT for the public clients/docs/skills repo (Copyright 2026 fifteenA, Inc.); the hosted phone fleet is commercial</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · openapi · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mobilebox.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mobilebox.dev/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mobilebox-dev/mobilebox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilebox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mobilebox is an agent-first cloud phone. The agent gets an Android 14 (arm64) sandbox, an iPhone or iPad simulator, or an optional real Android device, then reads the screen as numbered elements and taps, types, and swipes. `llms.txt`: *"Your agent supplies the reasoning; Mobilebox supplies the phone."*

Parked phones keep apps, data, and logins and are not billed. `llms.txt` states cloud Android at $0.01 per ready phone-minute (billed per second, one-minute minimum), large phones at $0.02, iPhone and iPad simulators at $0.03, and real Android devices at the cloud Android price. Check https://mobilebox.dev/llms.txt before relying on a price.

---

## Agent-facing interfaces

- **Interaction pattern:** agent-readable setup document + hosted MCP + REST. Not a one-URL join.
- **Catalog protocols:** Agent Skill, MCP, REST, openapi, http
- **MCP:** ✅ Available — hosted Streamable HTTP
- **Agent Skill:** ✅ Available — hosted skill.md (not an npx skills add registry package)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** agent-readable setup document + hosted MCP + REST. Not a one-URL join.

```bash
# Read https://mobilebox.dev/setup.md and follow it.
# MCP (Streamable HTTP): https://mobilebox.dev/mcp
#   Authorization: Bearer $MOBILESANDBOX_API_KEY
pip install mobilebox
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilebox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://mobilebox.dev/v1` with the same bearer key |
| OpenAPI | https://mobilebox.dev/openapi.json |
| Python client | `pip install mobilebox` |
| Hosted MCP | `https://mobilebox.dev/mcp` |
| Machine-readable docs | https://mobilebox.dev/llms.txt · https://mobilebox.dev/skill.md · https://mobilebox.dev/setup.md |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://mobilebox.dev
- https://mobilebox.dev/llms.txt
- https://mobilebox.dev/skill.md
- https://mobilebox.dev/setup.md
- https://mobilebox.dev/openapi.json
- https://mobilebox.dev/mcp
- https://github.com/mobilebox-dev/mobilebox

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
