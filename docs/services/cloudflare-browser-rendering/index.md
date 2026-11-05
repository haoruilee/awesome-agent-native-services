---
title: "Cloudflare Browser Rendering | Agent-Native Services"
service_name: "Cloudflare Browser Rendering"
description: "Headless browsers for AI agents (Cloudflare Workers)"
permalink: /services/cloudflare-browser-rendering/
page_kind: service
service_slug: "cloudflare-browser-rendering"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/cloudflare-browser-rendering.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/cloudflare-browser-rendering.md"
tagline: "Headless browsers for AI agents (Cloudflare Workers)"
website: "https://www.cloudflare.com/products/browser-rendering/"
repository: "https://github.com/cloudflare/workers-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.cloudflare.com/products/browser-rendering/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://developers.cloudflare.com/browser-run/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cloudflare/workers-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/cloudflare-browser-rendering.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cloudflare **Browser Rendering** provides **pooled headless Chrome** on Cloudflare's edge. Developers and **AI agents** automate navigation, screenshots, PDFs, markdown extraction, and structured extraction (including AI-assisted JSON from pages). In the Agents SDK, the newer **Browser Run** integration exposes a durable `browser_execute` tool where the model writes code against the Chrome DevTools Protocol (CDP), can inspect rendered pages, capture screenshots, debug frontend behavior, and keep live browser sessions across pauses for login, MFA, or approval. It scales to many concurrent isolated browser instances without agents running local Chrome.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API, documentation
- **MCP:** ✅ Playwright MCP integration documented for AI-driven browser control
- **Agent Skill:** ⚠️ No official npx skills add cloudflare/... bundle located for Browser Rendering.
- **Onboarding type:** `documentation`

## Protocol surface

| Interface | Detail |
|---|---|
| Workers + bindings | Puppeteer/Playwright from Worker code |
| Agents SDK Browser Run | Durable `browser_execute` tool and quick actions such as markdown/extract/links/scrape |
| REST API | [Browser Rendering API](https://developers.cloudflare.com/api/resources/browser_rendering/) |
| MCP | Playwright MCP per [AI guide](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
