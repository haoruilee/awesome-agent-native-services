---
title: "Framelink MCP for Figma | Agent-Native Services"
service_name: "Framelink MCP for Figma"
description: "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot"
permalink: /services/framelink-figma-mcp/
page_kind: service
service_slug: "framelink-figma-mcp"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/framelink-figma-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md"
tagline: "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot"
website: "https://www.framelink.ai/"
repository: "https://github.com/GLips/Figma-Context-MCP"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.framelink.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.framelink.ai/docs/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/GLips/Figma-Context-MCP" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Framelink MCP fetches **Figma file metadata via the Figma API** and **simplifies/translates** the payload so coding agents receive **layout- and styling-focused context** instead of noisy raw JSON. README positions it for **one-shot UI implementation** in agent mode when the user pastes a Figma link.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, STDIO, http, API
- **MCP:** ✅ MCP server (figma-developer-mcp)
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "Framelink MCP for Figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | stdio via `npx -y figma-developer-mcp …` |
| **Figma API** | https://www.figma.com/developers/api |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
