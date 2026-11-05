---
title: "MCP Toolbox for Databases | Agent-Native Services"
service_name: "MCP Toolbox for Databases"
description: "MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your…"
permalink: /services/google-mcp-toolbox/
page_kind: service
service_slug: "google-mcp-toolbox"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/google-mcp-toolbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md"
tagline: "MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your enterprise databases"
website: "https://mcp-toolbox.dev/"
repository: "https://github.com/googleapis/mcp-toolbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mcp-toolbox.dev/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mcp-toolbox.dev/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/googleapis/mcp-toolbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCP Toolbox exposes **database operations as MCP tools** in two modes: **prebuilt generic tools** (schema discovery, SQL execution, etc.) for fast IDE/agent connectivity, and a **custom tools framework** for production agents with **auth (including IAM)**, **restricted access**, **structured queries**, **semantic search**, **connection pooling**, and **OpenTelemetry** observability.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, SDK, http
- **MCP:** ✅ MCP server (@toolbox-sdk/server) + prebuilt database packs
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "toolbox-postgres": {
      "command": "npx",
      "args": ["-y", "@toolbox-sdk/server", "--prebuilt=postgres"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | `@toolbox-sdk/server` via npx |
| **SDKs** | Python, JS/TS, Go, Java |
| **Docs** | https://mcp-toolbox.dev/ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
