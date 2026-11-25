---
title: "Phone Harness | Agent-Native Services"
service_name: "Phone Harness"
description: "Let your agent use your phone"
permalink: /services/phone-harness/
page_kind: service
service_slug: "phone-harness"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/phone-harness.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phone-harness.md"
tagline: "Let your agent use your phone"
verified_at: "2026-11-25"
website: "https://phone-harness.com"
repository: "https://github.com/phone-harness/phone-harness"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (Copyright 2026 shawn pana)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://phone-harness.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://phone-harness.com/docs/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/phone-harness/phone-harness" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phone-harness.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Phone Harness lets an agent tap, type, scroll, and read a phone screen. Locally that is the operator's iPhone through iPhone Mirroring, or an Android device over adb. In the cloud, the API can start a temporary Android emulator or a saved Android phone, and it can attach a hosted iPhone. Docs (https://phone-harness.com/docs/llms.txt) describe shared Android emulators and real Cloud iPhones on a flat subscription, with an optional viewer for video or a still screenshot.

The OpenClaw guide on that index says every script asks the person first. That is a property of the OpenClaw integration, not of every API call. The session API and hosted MCP do not require a human click for each tap. A viewer can watch.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + REST + hosted MCP, after a dashboard key. Not a one-URL join.
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, http, API
- **MCP:** ✅ Available — hosted Streamable HTTP for cloud phones
- **Agent Skill:** ✅ Available — SKILL.md in the repo and a docs-site skill
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + REST + hosted MCP, after a dashboard key. Not a one-URL join.

```bash
pip install phone-harness
# Hosted MCP (cloud phones only): https://mcp.phone-harness.com/mcp
# REST base: https://api.phone-harness.com
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phone-harness.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `pip install phone-harness` |
| REST | `https://api.phone-harness.com` — bearer API key |
| Hosted MCP | `https://mcp.phone-harness.com/mcp` |
| Docs index | https://phone-harness.com/docs/llms.txt |
| Skills | Repo `SKILL.md` and https://phone-harness.com/docs/skill.md |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://phone-harness.com
- https://phone-harness.com/docs/llms.txt
- https://phone-harness.com/docs/skill.md
- https://mcp.phone-harness.com/mcp
- https://github.com/phone-harness/phone-harness

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
