---
title: "Chrome DevTools MCP | Agent-Native Services"
service_name: "Chrome DevTools MCP"
description: "chrome-devtools-mcp lets your coding agent (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser"
permalink: /services/chrome-devtools-mcp/
page_kind: service
service_slug: "chrome-devtools-mcp"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md"
tagline: "chrome-devtools-mcp lets your coding agent (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser"
website: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
repository: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (per repository)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Chrome DevTools MCP exposes **live Chrome** to coding agents through the Model Context Protocol: **Puppeteer-driven automation** with waits for action results, **DevTools-level debugging** (network, console with source maps, screenshots), and **performance tooling** (traces and lab/field insights). It is explicitly built so **coding agents** can drive and inspect a real browser session rather than guessing from static HTML.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, STDIO
- **MCP:** ✅ This project is an MCP server
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | stdio server launched with `npx -y chrome-devtools-mcp@latest` |
| **npm** | Package `chrome-devtools-mcp` |
| **Chrome** | Official support for Google Chrome and Chrome for Testing |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
