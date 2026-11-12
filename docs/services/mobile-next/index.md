---
title: "Mobile Next | Agent-Native Services"
service_name: "Mobile Next"
description: "Real iOS and Android devices for AI agents"
permalink: /services/mobile-next/
page_kind: service
service_slug: "mobile-next"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/mobile-next.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobile-next.md"
tagline: "Real iOS and Android devices for AI agents"
verified_at: "2026-11-12"
website: "https://mobilenext.ai"
repository: "https://github.com/mobile-next/mobile-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (open-source Mobile MCP)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · openapi · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-12</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mobilenext.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mobilenext.ai/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mobile-next/mobile-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobile-next.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mobile Next is a programmable mobile runtime for AI agents. The open-source Mobile MCP server attaches to a simulator, emulator, or cable-connected phone and lets an agent read the accessibility tree, tap, type, swipe, install and launch apps, and record the screen. Mobile Next Cloud is the same control surface on hosted real iOS and Android devices, billed per minute, over a hosted MCP server and a REST API.

Mobilewright sits on top when a working agent flow should become a repeatable CI test.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (local stdio or hosted Streamable HTTP) + REST API.
- **Catalog protocols:** MCP, REST, openapi, STDIO, http
- **MCP:** ✅ Available (open-source stdio + hosted Cloud MCP)
- **Agent Skill:** ⚠️ No official npx skills add package was found on the pages reviewed. The Claude Code plugin (mobile-mcp@mobile-mcp) and /mobile-mirror are the documented agent install path for the local server.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (local stdio or hosted Streamable HTTP) + REST API.

```bash
npx @mobilenext/mobile-mcp@latest install
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobile-next.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Local MCP | `npx -y @mobilenext/mobile-mcp@latest` (stdio) |
| Cloud MCP | `https://app.mobilenext.ai/mcp` |
| REST | `https://app.mobilenext.ai` — OpenAPI at https://mobilenext.ai/openapi.json |
| Docs | https://mobilenext.ai/docs/ · https://mobilenext.ai/llms.txt |

---

## Verification

Last verified **2026-11-12**.

Sources:
- https://github.com/mobile-next/mobile-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
