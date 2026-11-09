---
title: "three.ws | Agent-Native Services"
service_name: "three.ws"
description: "The 3D Agent Layer of the Internet"
permalink: /services/three-ws/
page_kind: service
service_slug: "three-ws"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/three-ws.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/three-ws.md"
tagline: "The 3D Agent Layer of the Internet"
verified_at: "2026-11-07"
website: "https://three.ws"
repository: "https://github.com/nirholas/three.ws"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (public repository)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-07</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://three.ws" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://three.ws/grok · https://three.ws/grok-skill.md · https://three.ws/connect · https://three.ws/docs/grok-bot.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/nirholas/three.ws" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/three-ws.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

three.ws gives agents a 3D studio and optional body: generate a textured GLB + viewer link from a prompt, rig a humanoid avatar, search ready-made CC0 assets, and create a speaking persona. Long GPU jobs return within a short timeout with a job id for `check_job` polling so agent tasks do not hang. Signed-in surfaces add agent runtime (memory, skills) and read-only market intel; spending tools are excluded from the Grok connector per product docs.

---

## Agent-facing interfaces

- **Interaction pattern:** Remote MCP (+ Grok skill URL)
- **Catalog protocols:** Agent Skill, MCP, http, API
- **MCP:** ✅ Available — Grok-dedicated remote endpoint
- **Agent Skill:** ✅ Hosted skill document for Grok / Grok Bot
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Remote MCP (+ Grok skill URL)

```
https://three.ws/api/mcp-grok
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/three-ws.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (Grok) | https://three.ws/api/mcp-grok |
| Skill | https://three.ws/grok-skill.md |
| Docs | https://three.ws/grok · https://three.ws/docs/grok-bot.md · https://three.ws/connect |
| Repo | https://github.com/nirholas/three.ws |

---

## Verification

Last verified **2026-11-07**.

Sources:
- https://three.ws/grok-skill.md
- https://three.ws/api/mcp-grok

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
