---
title: "Limrun | Agent-Native Services"
service_name: "Limrun"
description: "Unlock cloud agents for mobile dev teams"
permalink: /services/limrun/
page_kind: service
service_slug: "limrun"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/limrun.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/limrun.md"
tagline: "Unlock cloud agents for mobile dev teams"
verified_at: "2026-11-12"
website: "https://limrun.com"
repository: "https://github.com/limrun-inc"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-12</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://limrun.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.limrun.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/limrun-inc" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/limrun.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Limrun gives a cloud or CI agent a remote Xcode Mac, an iOS simulator, and an Android emulator it can drive from Linux, Windows, or a sandbox that has no local device tooling. The agent creates an instance over MCP, reads the accessibility tree and screenshots, taps and types, records video, and deletes the instance when done. Remote Xcode and Gradle builds, PR preview links, and demo videos sit beside that control plane.

---

## Agent-facing interfaces

- **Interaction pattern:** remote MCP (OAuth or API key) + lim CLI + published skills.
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, openapi, http, API
- **MCP:** ✅ Available (hosted remote + per-instance)
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** remote MCP (OAuth or API key) + lim CLI + published skills.

```bash
claude mcp add --transport http limrun https://mcp.limrun.com/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/limrun.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.limrun.com/mcp` |
| Per-instance MCP | `status.mcpUrl` + `status.token` |
| CLI | `npm install -g lim` / `brew install limrun-inc/tap/lim` |
| REST / SDKs | https://api.limrun.com — OpenAPI at https://limrun.com/openapi.json; TS/Python/Go SDKs |
| Skills | `npx skills add limrun-inc/skills` or `lim skills install` |

---

## Verification

Last verified **2026-11-12**.

Sources:
- https://github.com/limrun-inc

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
