---
title: "Arcade | Agent-Native Services"
service_name: "Arcade"
description: "MCP tools with managed OAuth — credentials stay out of the LLM"
permalink: /services/arcade/
page_kind: service
service_slug: "arcade"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/arcade.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md"
tagline: "MCP tools with managed OAuth — credentials stay out of the LLM"
website: "https://www.arcade.dev"
repository: "https://github.com/ArcadeAI/arcade-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.arcade.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.arcade.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ArcadeAI/arcade-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Arcade helps teams ship **production MCP servers** where tools call third-party APIs with **OAuth on behalf of end users**, while **secrets and tokens never enter the LLM context**. Docs emphasize **user-facing agents**, **authorized tool calling**, and **SSO for AI agents** — bridging agent intent, user consent, and least-privilege API access.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Arcade *is* an MCP authoring and hosting platform
- **Agent Skill:** ⚠️ No official npx skills add ArcadeAI/... bundle located.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
uv tool install arcade-mcp
arcade new my_server
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | Primary agent integration |
| Arcade CLI | `arcade new`, deploy, local dev |
| HTTP APIs | Arcade Cloud for hosted servers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
