---
title: "Playwright MCP | Agent-Native Services"
service_name: "Playwright MCP"
description: "A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright"
permalink: /services/playwright-mcp/
page_kind: service
service_slug: "playwright-mcp"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/playwright-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md"
tagline: "A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright"
website: "https://playwright.dev/docs/getting-started-mcp"
repository: "https://github.com/microsoft/playwright-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://playwright.dev/docs/getting-started-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://playwright.dev/mcp/configuration/options" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/microsoft/playwright-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Playwright MCP exposes browser automation as MCP tools so coding agents can open pages, inspect structure, click/type, and extract information from real web sessions. It uses accessibility snapshots and structured tool responses, reducing reliance on pixel-based screenshot interpretation.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP server (stdio by default; optional HTTP transport)
- **Catalog protocols:** MCP, STDIO, http
- **MCP:** ✅ Native MCP server
- **Agent Skill:** ⚠️ No standalone SKILL.md package found from the Playwright MCP repository.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP server (stdio by default; optional HTTP transport)

```bash
npx @playwright/mcp@latest
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP stdio | `npx @playwright/mcp@latest` |
| MCP HTTP | `--port` mode, e.g. `http://localhost:8931/mcp` |
| npm package | `@playwright/mcp` |
| Docker | `mcr.microsoft.com/playwright/mcp` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
